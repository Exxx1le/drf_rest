import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from './components/users';
import ProjectList from './components/projects';
import NotFound404 from './components/notfound404';
import ProjectListAuthors from './components/ProjectsAuthors';
import { BrowserRouter, Route, Link, Switch, Redirect } from 'react-router-dom'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'users': [],
      'projects': []
    }
  }

  componentDidMount() {
    //const users = [
    //  {
    //    'first_name': 'Иван',
    //    'last_name': 'Иванов'
    //  },
    //  {
    //    'first_name': 'Петр',
    //    'last_name': 'Петров'
    //  }
    //]
    axios.get('http://127.0.0.1:8000/api/users/').then(response => {
      this.setState(
        {
          'users': response.data
        }
      )
    }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/projects/').then(response => {
      this.setState(
        {
          'projects': response.data
        }
      )
    }).catch(error => console.log(error))


  }


  render() {
    return (
      <div>
        <BrowserRouter>
          <nav>
            <ul>
              <li>
                <Link to='/'>Users</Link>
              </li>
              <li>
                <Link to='/projects'>Projects</Link>
              </li>
            </ul>
          </nav>
          <Switch>
            <Route exact path='/' component={() => <UserList users={this.state.users} />} />
            <Route exact path='/projects' component={() => <ProjectList users={this.state.projects} />} />
            <Route path='/user/:id'>
              <ProjectListAuthors projects={this.state.projects} />
            </Route>
            <Redirect from='/project' to='/projects' />
            <Route component={NotFound404} />
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
