// src/routes.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import App from './App';

const Routes = () => (
    <Router>
        <Switch>
            <Route path="/" component={App} />
        </Switch>
    </Router>
);

export default Routes;
