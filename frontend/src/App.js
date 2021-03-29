import React from "react";
import './App.css';
import AuthorList from "./components/Author";
import axios from "axios";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'authors': []
    };
  }

  componentDidMount() {
    axios.get('http://localhost:8000/api/authors')
      .then(response => {
        const authors = response.data;
        this.setState({
          'authors': authors
        }
        );
      }).catch(error => console.log(error));
  }

  render() {
    return (
      <div>
        <AuthorList authors={this.state.authors}/>
      </div>
    );
  }
}

export default App;
