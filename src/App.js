import React, { Component } from 'react';
import logo from './logo.svg';
import clubLogo from './codersSBlogo.png';
import './App.css';

class App extends Component {
	  render() {
		      return (
			            <div className="App">
			              <header className="App-header">
			                <img src={clubLogo} style={{height:100}}  className="App-logo" alt="logo" />
			                <p>
			                There is a light at the edge of sight, where the sea kisses the sky... 
			                </p>
			               <a
			                  className="App-link"
			                  href="https://reactjs.org"
			                  target="_blank"
			                  rel="noopener noreferrer"
			                >
			      		<p style={{textAlign:"left", fontFamily:"monospace"}}  >EtymologyTeam = [Benjamin Hsieh, Sean Carter, Connor Duncan, Sophia Weiler]</p>
			      		<p style={{textAlign:"left", fontFamily:"monospace"}} >return(EtymologyTeam == teams.best);</p>
			      		<p style={{textAlign:"left", fontFamily:"monospace"}} >>>> True</p>
			      </a>
			              </header>
			      
			      	</div>
			          );
		    }
}

export default App;


















