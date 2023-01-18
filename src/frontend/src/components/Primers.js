import { Component } from "react";
import './Primers.css'
import EndPrimers from './EndPrimers'
import {Dna} from "react-loader-spinner";

class Primers extends Component{
    constructor(props) {
        super(props);
        this.state = {
            location: "",
            primer: "",
            endprimers: {location: "", primer: "",},
            loading: false,
        };

        this.handleClick = this.handleClick.bind(this);

    }

    async handleClick(event){
        event.preventDefault();
        const location = event.target.getAttribute("location");
        const primer = this.props.primers[location];
        await this.setState({
            location: location,
            primer: primer,
        });

        this.setState({loading:true});
        await fetch('/endprimers',{
            method: 'post',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify({
                "location": this.state.location,
                "primer": this.state.primer
            })
        })
            .then((response)=> response.json())
            .then((primers)=>{
                this.setState({
                    endprimers: primers
                });
            });
        this.setState({loading:false});
    }

    render() {
        const primers = this.props.primers;
        const locations = Object.keys(primers);
        const listItems = locations.map((location)=>
            <li key={location}>
                <a href="#" onClick={this.handleClick} location={location}> {location+' >'} {primers[location]} </a>
            </li>)


        return(
            <div className="primers-container">
                <div className='primers'>
                    <ul>
                        {listItems}
                    </ul>
                </div>
                <div className="loading">
                        <Dna
                            visible={this.state.loading}
                            height="80"
                            width="80"
                            ariaLabel="dna-loading"
                            wrapperStyle={{}}
                            wrapperClass="dna-wrapper"
                        />
                    </div>
                <EndPrimers endprimers={this.state.endprimers}/>
            </div>
        )
    }
}

export default Primers;