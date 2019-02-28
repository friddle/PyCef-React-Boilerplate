import { observable, action } from 'mobx';

export default class HelloModel {

  @observable world;
  constructor() {
    this.world = 'Message Send To Python';
  }

  @action.bound
  setWorld(world) {
    this.world = world;
  }

  @action
  fetchHello(){
      window.Hello.hello("from python",(result)=>{this.setWorld(result)})
  }
}