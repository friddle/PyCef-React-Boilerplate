import { observable, action } from 'mobx';

export default class HelloModel {

  @observable world;
  constructor() {
    this.world = '';
    this.times=1
  }

  @action.bound
  setWorld(world) {
    this.world = world;
  }

  @action.bound
  addTimes(times)
  {
    this.times=this.times+1
  }

  @action
  fetchHello(){
      window.HelloWorld.hello((result)=>{console.log("result");this.setWorld(result)})
  }
}