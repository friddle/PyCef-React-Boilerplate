import React, { Component } from 'react';
import { observer } from 'mobx-react';
import styles from './Hello.css';

@observer
class Hello extends React.Component {
    constructor(props) {
        super(props);
    }
    onClick(){
        this.props.store.fetchHello();
    }
   render() {
       const { world } = this.props.store;
       return (
           <div>
               <div>
                   <div className={styles.container} data-tid="container">
                       <h3>{world}</h3>
                       <p>check HelloWorld.py from package:src.hello</p>
                       <button onClick={this.onClick.bind(this)}>PythonGet</button>
                   </div>
               </div>
           </div>);
   }
}

export default Hello;