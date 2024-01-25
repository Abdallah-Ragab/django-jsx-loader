import subprocess
from django import template
from django.conf import settings
import os
import random
import string


register = template.Library()


@register.tag(name="jsx")
def do_jsx(parser, token):
    nodelist = parser.parse(("endjsx",))
    parser.delete_first_token()
    return JsxNode(nodelist)


class JsxNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

        self.pre_bundle_dir = self.get_dir("prebundle")
        self.post_bundle_dir = self.get_dir("postbundle")
        self.id = self.generate_random_id()
        self.pre_bundle_file = os.path.join(self.pre_bundle_dir, self.id + ".jsx")
        self.jsx_content = self.nodelist.render({})

    def write_file(self, filename, content):
        try:
            with open(filename, "w") as file:
                file.write(content)
                return filename
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print(f"Error: {str(e)}")
        return False

    def get_dir(self, name):
        path = os.path.join(settings.BASE_DIR, name)

        if not os.path.exists(path):
            os.makedirs(path)

        return path

    def generate_random_id(self):
        id = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return id

    def generate_placeholder_element(self):
        return f'<div id="{self.id}"></div>'

    def bundle_jsx_file(self, config_file):
        output_file = os.path.join(self.post_bundle_dir, self.id + ".js")
        # command = f"npx webpack --mode development --entry {self.pre_bundle_file} --output-path {self.post_bundle_dir} --output-filename {self.id}.js --module-bind js=babel-loader"
        command = f"npx webpack --mode development --entry {self.pre_bundle_file} --output-path {self.post_bundle_dir} --output-filename {self.id}.js --module-bind js=babel-loader"
        print(command)
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        try:
            result.check_returncode()
        except subprocess.CalledProcessError:
            print(f"Error bundling the jsx file #{self.id}: \n{result.stderr}")

        return output_file

    def generate_config_file(self):
        config_file = os.path.join(self.pre_bundle_dir, "webpack.config.js")
        config_content = """
        module.exports = {
            entry: '{}/{}.jsx',
            output: {
                path: '{}',
                filename: '{}.js',
                target: 'amd',
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
        """.format(self.pre_bundle_dir, self.id, self.post_bundle_dir, self.id)
        return self.write_file(config_file, config_content)

    def render(self, context):
        if self.write_file(self.pre_bundle_file, self.jsx_content):
            self.bundle_jsx_file()


            return self.generate_placeholder_element()
        return ""


# TODO : Configuration option to choose output location. default: /static/
# TODO: Add option in tag declaration for naming the JSX Component instead of using random.
