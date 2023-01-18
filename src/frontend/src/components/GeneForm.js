import { Component } from "react";
import './GeneForm.css'
import { Dna } from  'react-loader-spinner'


class GeneForm extends Component{
    constructor(props) {
        super(props);
        this.state = {
            inputType: "id",
            inputID: "NM_000875.5",
            loading: false,
            gene_raw: "",
        };

        this.inputType = this.inputType.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handleRawChange = this.handleRawChange.bind(this);
    }

    inputType(event){
        this.setState({
            inputType: event.target.value,
        });
    }

    handleChange(event) {
        this.setState({inputID: event.target.value});
    }

    handleRawChange(event){
        this.setState({gene_raw: event.target.value})
    }

    async handleSubmit(event) {
        event.preventDefault();

        this.setState({loading:true});
        if (this.state.inputType === "id"){

            await fetch('/id', {
                method: 'post',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify({
                    "ncbi_id": this.state.inputID
                })
            })
                .then((response) => response.json())
                .then((primers) => {
                    this.props.onUpdate(primers)
                });

        } else {
            if (Array.from(this.state.gene_raw)[0]===">") {
                await fetch('/raw',{
                    method: 'post',
                    headers: {'Content-Type':'application/json'},
                    body: JSON.stringify({
                        "gene_raw": this.state.gene_raw
                    })
                })
                    .then((response)=> response.json())
                    .then((primers)=>{
                        this.props.onUpdate(primers)
                    });
            }
        }
        this.setState({loading:false});

    }

    render(){
        const { inputType } = this.state;

        let inputArea;

        if (inputType === 'id'){
            inputArea = <input type='text' className='input-id' placeholder="NM_000875.5" onChange={this.handleChange}/>
        }else{
            inputArea = <textarea className='input-raw' onChange={this.handleRawChange}/>
        }

        return(
            <div>
                <form onSubmit={this.handleSubmit} className="gene-form">
                    <div className="input-choice">
                        <label htmlFor="choiceId">
                            Search with NCBI ID
                            <input type="radio" name="input type" id="choiceId" value='id' onChange={this.inputType} defaultChecked/>
                        </label>
                        <label htmlFor="choiceRaw">
                            Enter Manually
                            <input type="radio" name="input type" value='raw' onChange={this.inputType} id="choiceRaw" />
                        </label>
                    </div>
                    <span>Active Search: {this.state.inputID}</span>
                    {inputArea}
                    <input type="submit" className="submit-button" value="Find Primers🧬"/>
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

                    <ul>
                        <li>Length of primers is between 18 and 30 bases</li>
                        <li>GC content is between 40% and 60%</li>
                        <li>Primers end with G or C</li>
                        <li>Melting temperature(Tm) of primers is between 55°C and 65°C</li>
                        <li>Melting temperature(Tm) is within 5°C between start and end primers</li>
                        <li>Avoid runs of 4 or more of one base</li>
                        <li>Avoid di-nucleotide repeats of 4 or more times</li>
                        <li>Avoid intra-primer, and inter-primer homology</li>
                    </ul>
                </form>
            </div>
        )
    }
}

export default GeneForm;