import {Component} from "react";
import './EndPrimers.css'
 
class EndPrimers extends Component{


    render(){
        const primers = this.props.endprimers;
        const locations = Object.keys(primers);
        const listItems = locations.map((location)=>
            <li key={location}>
                <a location={location}> {location+' >'} {primers[location]} </a>
            </li>)
        return(
            <div className='endprimers' >
                <ul>
                    {listItems}
                </ul>
            </div>
        )
    }
}

export default EndPrimers;