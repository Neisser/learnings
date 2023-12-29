import { runInNewContext } from 'vm';

const ContextObject = runInNewContext('Object');

console.log(Object === ContextObject);

console.log(new Object() instanceof ContextObject );

console.log(ContextObject.name);