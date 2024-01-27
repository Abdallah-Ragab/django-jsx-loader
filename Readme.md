## Install :
```bash
pip install django-jsx-loader
```

install npm dependencies

```bash
npm install --save-dev babel-loader @babel/preset-env @babel/preset-react webpack-cli react react-dom
```
## Setup :
```python
# settings.py
INSTALLED_APPS = [
    ...
    'django_jsx_loader',
    ...
]
```

## Configuration :

You can change configuration inside django's `settings.py`

***All paths are relative to the base directory of the project(where manage.py is)*


```python
# settings.py

JSX_LOADER = {
    'base_dir': 'frontend',
    'output_dir': 'output',
    ...
}
```

### Configuration Options :


Configration | Type | Description | Default
--- | --- | --- | ---
base_dir | String | The name of the directory housing all other directories related to the jsx loader. | jsx_modules
output_dir | String | The name of the directory where the output javascript files will be placed. | static


## Usage :

- ### Inline JSX :
```html
<!-- template.html -->
{% load jsx_loader %}
{% JSX %}
    <div className="Component">
        <h1>Hi, I'm a React App</h1>
    </div>
{% endJSX %}
```

- ### Jsx Component File :

```html
<!-- template.html -->
{% load jsx_loader %}
{% JSXComponentFile 'components/counter.jsx' %}
```

- ### Inline Jsx Component :

```html
<!-- template.html -->
{% load jsx_loader %}
{% JSXComponent %}
    import
    const Counter = () => {
        const [count, setCount] = useState()
        return (
            <div className="Counter">
                <h1>Hi, I'm a React Counter</h1>
                <h2>{count}</h2>
                <button onClick={() => setCount(count + 1)}>+</button>
            </div>
        );
    }

    export default Counter;
{% endJSXComponent %}
```

## Loading Steps :
- Tag Content is copied to a temp file
  ```
    <!-- temp file -->
    const componentID = () => {
        return (
            <!-- Copied JSX from JSX tag -->
            <div className="Component">
                <h1>Hi, I'm a React App</h1>
            </div>
        );
    }

    export default componentID;
  ```
- Component Rendering Script Is Made
  ```
  import JSXComponent from 'temp.component.file'
  import AnotherComponent from 'another.temp.file'
  import reactDOM from 'react-dom'

  reactDOM.render(<JSXComponent />, document.getElementById('component-id'))
  reactDOM.render(<AnotherComponent />, document.getElementById('another-component-id'))
  ```

- Tags are replaced with placeholder HTML elements.
  ```
  <div id="component-id"></div>
  ```
- Webpack Config file is made with Rendering Script as entry point
- webpack command is run
- output script file is added to the template
  ```
  <script src="{% static 'output.js' %}"></script>
  ```

#### *****All the steps should be done manually in production by running a command except for tags replacement.***