import React, { Component } from "react";
import './App.css'
import GeneForm from "./components/GeneForm";
import Primers from "./components/Primers";


class App extends Component{
    constructor(props) {
        super(props);

        this.state = {
            primers: { index: 'primer sequence' }
        };

        this.onUpdate = this.onUpdate.bind(this)
    }

    onUpdate(data){
        this.setState({primers:data});
    }

    render() {
        return(
            <div className='base'>
                <GeneForm onUpdate = { this.onUpdate }/>
                <Primers primers = { this.state.primers }/>
            </div>

        )
    }
}

export default App;
