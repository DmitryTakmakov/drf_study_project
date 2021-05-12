import React from "react";
import './App.css';
import UsersList from "./components/User";
import HeaderMenu from "./components/Header";
import axios from "axios";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'users': [],
      'apis': []
    };
  }

  componentDidMount() {
    axios.get('http://localhost:8000/api/')
      .then(response => {
        const available_api_array = Object.keys(response.data);
        this.setState({
          'apis': available_api_array
        });
      }).catch(error => console.log(error));
    axios.get('http://localhost:8000/api/users')
      .then(response => {
        const users = response.data;
        this.setState({
          'users': users
        }
        );
      }).catch(error => console.log(error));
  }

  render() {
    return (
      <div>
        <HeaderMenu apis={this.state.apis}/>
        <UsersList users={this.state.users}/>
      </div>
    );
  }
}

export default App;
