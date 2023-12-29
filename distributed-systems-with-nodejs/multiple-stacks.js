function a(){
  console.log('function a');
  b();
}

function b(){
  console.log('function b');
  c();
}

function c(){
  console.log('function c');
}

function x(){
  console.log('function x');
  y();

}

function y(){
  console.log('function y');
  z();
}

function z(){
  console.log('function z');
}

function o(){
  console.log('function o');
  p();
}

function p(){
  console.log('function p');
  q();
}

function q(){
  console.log('function q');
}

function req(seed){
  console.log('epoch: ', seed);
  if(seed === 10){
    console.log('finish')
  }
  seed++;

  req(seed);
}

function iterator(){
  for (let index = 0; index < 10; index++) {
    console.log('epoch: ', index);
    
  }
}

// setTimeout(x, 0)
// a();
// o();
// req(0)
iterator();
