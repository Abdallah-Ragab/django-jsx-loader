from ..config import Config
import subprocess
from django import template
from django.conf import settings
import os
import random
import string
from pathlib import Path

class JSXNode(template.Node):
    def increase_node_count (self):
        self.context["jsx_loader"]["_counter"] += 1

    def get_index(self):
        return self.context["jsx_loader"]["_counter"]

    def get_template_path(self):
        return self.context.template.origin.name

    def get_template_name(self):
        return self.context.template.name

    def render(self, context) -> str:
        self.context = context
        self.template_path = self.get_template_path()
        self.template_name = self.get_template_name()
        self.increase_node_count()
        self.index = self.get_index()



class JsxNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
        self.config = Config()

        self.base_dir = self.config.base_dir
        self.pre_bundle_dir = self.get_dir(self.config.pre_bundle_dir)
        self.post_bundle_dir = self.get_dir(self.config.post_bundle_dir)
        self.config_dir = self.get_dir(self.config.config_dir)

        self.id = self.generate_random_id()
        self.pre_bundle_file = self.pre_bundle_dir.joinpath(self.id + ".jsx")
        self.post_bundle_file = self.post_bundle_dir.joinpath(self.id + ".js")
        # self.content = self.nodelist.render({})

    def write_file(self, path, content):
        try:
            with open(path, "w") as file:
                file.write(content)
                return path
        except FileNotFoundError:
            print(f"Error writing '{path}' file: File not found.")
        except PermissionError:
            print(f"Error writing '{path}' file: Permission denied.")
        except Exception as e:
            print(f"Error writing '{path}' file: {str(e)}")
        return False

    def get_dir(self, name):
        project_path = Path(settings.BASE_DIR)
        base_path = project_path.joinpath(self.base_dir)
        path = base_path.joinpath(name)

        if not path.exists:
            os.makedirs(path, exist_ok=True)

        return path

    def generate_random_id(self):
        id = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return id

    def generate_placeholder_element(self):
        return f'<div id="{self.id}"></div>'

    def bundle_jsx_file(self):
        output_file = self.post_bundle_dir.joinpath(self.id + ".js")

        # command = f"npx webpack --mode development --entry {self.pre_bundle_file} --output-path {self.post_bundle_dir} --output-filename {self.id}.js --module-bind js=babel-loader"
        command = f'npx --yes webpack --mode development --config "{self.config_file}"'
        print(command)
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        try:
            result.check_returncode()
        except subprocess.CalledProcessError:
            print(f"Error bundling the jsx file #{self.id}: \n{result.stderr}")

        return output_file

    def generate_config_file(self):
        config_file = self.pre_bundle_dir.joinpath(f"{self.id}.config.js")

        config_content = (
            """
        module.exports = {
            entry: '"""
            + self.pre_bundle_file.as_posix()
            + """',
            output: {
                path: '"""
            + self.post_bundle_dir.as_posix()
            + """',
                filename: '"""
            + self.id
            + ".js"
            + """',
            },
            module: {
                rules: [
                    {
                        test: /\.jsx?$/,
                        exclude: /(node_modules)/,
                        use: {
                            loader: 'babel-loader',
                            options: {
                                presets: ['@babel/preset-env', '@babel/preset-react']
                            }
                        }
                    }
                ]
            }
        };
        """
        )
        return self.write_file(config_file, config_content)

    def generate_jsx_render_js_file(self, target_id, jsx_content):
        render_js_file = self.post_bundle_dir.joinpath(f"{self.id}.js")

        render_js_content = f"""
        import React from 'react';
        import ReactDOM from 'react-dom';
        import Component from '{self.post_bundle_file}';

        ReactDOM.render(<Component />, document.getElementById('{target_id}'));
        """
        return self.write_file(render_js_file, render_js_content)

    def render(self, context):
        self.content = self.nodelist.render(context)
        if self.write_file(self.pre_bundle_file, self.content):
            self.config_file = self.generate_config_file()
            self.bundle_jsx_file()

            return self.generate_placeholder_element()
        return ""
