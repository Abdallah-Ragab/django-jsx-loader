## Install:
```bash
pip install django-jsx-loader
```

```bash
npm install --save-dev babel-loader @babel/preset-env @babel/preset-react webpack-cli react react-dom
```
## Setup:
```python
# settings.py
INSTALLED_APPS = [
    ...
    'django_jsx_loader',
    ...
]
```


## Usage:

- ### Inline JSX
```html
<!-- template.html -->
{% load jsx_loader %}
{% JSX %}
    <div className="Component">
        <h1>Hi, I'm a React App</h1>
    </div>
{% endJSX %}
```

- ### Jsx Component File

```html
<!-- template.html -->
{% load jsx_loader %}
{% JSXComponentFile 'components/counter.jsx' %}
```

- ### Inline Jsx Component

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
```html

## Tags Types:
- ### JSX Syntax :

  ```
  {% JSX %}

    <div className="Component">
        <h1>Hi, I'm a React App</h1>
    </div>

  {% endJSX %}
  ```
  Cons
    - No way to import components
    - No way to use state
    - No way to use lifecycle methods



- ### Inline JSX Component :
  ```
  {% JSXComponent %}

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


- ### Link to a JSX Component file :
    ```
    {% JSXComponentFile 'components/counter.jsx' %}
    ```
- ### Static tag to import the bundled script
  ```
  {%  %}
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