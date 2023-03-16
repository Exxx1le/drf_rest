import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from './components/users';
import ProjectList from './components/projects';
import NotFound404 from './components/notfound404';
import ProjectListAuthors from './components/ProjectsAuthors';
import LoginForm from './components/Auth';
import Cookies from 'universal-cookie';
import { BrowserRouter, Route, Link, Switch, Redirect } from 'react-router-dom'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'users': [],
      'projects': [],
      'token': ''
    }
  }

  load_data() {
    const headers = this.get_headers()
    axios.get('http://127.0.0.1:8000/api/users/', { headers }).then(response => {
      this.setState(
        {
          'users': response.data
        }
      )
    }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/projects/', { headers }).then(response => {
      this.setState(
        {
          'projects': response.data
        }
      )
    }).catch(error => console.log(error))
  }

  set_token(token) {
    // localStorage.setItem('token', token)
    // let item = localStorage.getItem('token')
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({ 'token': token }, () => this.load_data())

  }

  get_token(username, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/',
      { 'username': username, 'password': password }).then(response => {
        this.set_token(response.data['token'])
      }).catch(error => alert('Не верный логин или пароль'))
  }

  is_auth() {
    return !!this.state.token
  }

  get_headers() {
    let headers = {
      'Content-Type': 'application/json'
    }

    if (this.is_auth()) {
      headers['Authorization'] = `Token ${this.state.token}`
    }

    return headers
  }

  logout() {
    this.set_token('')
  }

  get_token_from_cookies() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({ 'token': token }, () => this.load_data())
  }

  componentDidMount() {
    //   //const users = [
    //   //  {
    //   //    'first_name': 'Иван',
    //   //    'last_name': 'Иванов'
    //   //  },
    //   //  {
    //   //    'first_name': 'Петр',
    //   //    'last_name': 'Петров'
    //   //  }
    //   //]
    this.load_data()
  }

  deleteProject(id) {
    const headers = this.get_headers()
    axios.delete(`http://127.0.0.1:8000/api/projects/${id}`, { headers, headers })
      .then(response => {
        this.setState({ projects: this.state.projects.filter((item) => item.id !== id) })
      }).catch(error => console.log(error))
  }

  createProject(name, author) {
    const headers = this.get_headers()
    const data = { name: name, author: author }
    axios.post(`http://127.0.0.1:8000/api/projects/`, data, { headers, headers })
      .then(response => {
        let new_project = response.data
        const author = this.state.authors.filter((item) => item.id === new_project.author)[0]
        new_project.author = author
        this.setState({ projects: [...this.state.projects, new_project] })
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
              <li>
                {this.is_auth() ? <button onClick={() => this.logout()}>Logout</button> :
                  <Link to={'/login'}>Login</Link>}
              </li>
            </ul>
          </nav>
          <Switch>
            <Route exact path='/' component={() => <UserList users={this.state.users} />} />
            <Route path='/user/:id'>
              <ProjectListAuthors projects={this.state.projects} />
            </Route>
            <Route exact path='/login' component={() => <LoginForm get_token={(username, password) =>
              this.get_token(username, password)} />} />
            <Redirect from='/project' to='/projects' />
            <Route component={NotFound404} />
            <Route exact path='/projects/create' component={() => <ProjectForm />} />
            <Route exact path='/projects' component={() => <ProjectList
              items={this.state.projects} deleteProject={(id) => this.deleteProject(id)} />} />
            <Route exact path='/projects/create' component={() => <ProjectForm
              authors={this.state.authors} createProject={(name, author) => this.createProject(name, author)} />} />
          </Switch>
        </BrowserRouter>
      </div >
    );
  }
}

export default App;
