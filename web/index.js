import React from 'react';
import ReactDOM from 'react-dom';
import { Router } from 'react-router';
import createBrowserHistory from 'history/createBrowserHistory';
import './template/app.global.css';
import App from './render/App';

const history = createBrowserHistory({
  hashType: 'slash'
});

window.history_api = history;

ReactDOM.render(
  <Router history={history} >
    <App />
  </Router>
  , document.getElementById('root')
)
