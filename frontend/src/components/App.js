import React, { Component } from "react";
import { render } from "react-dom";
export default class App extends Component{
    constructor(props){
        super(props);

    }
    render(){
        return <h1>Hello World</h1>;
    }
}
ReactDOM.createRoot(document.getElementById('app')).render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
)
