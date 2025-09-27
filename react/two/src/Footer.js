import React from "react";


class Footer extends React.Component{
    render(){
        let {text} = this.props
        return(
            <footer style={{background: 'red', padding: '20px 0', fontSize: '20px', color: 'white'}}>
                <p>{text}</p>
            </footer>
        )
    }
}

export default Footer;