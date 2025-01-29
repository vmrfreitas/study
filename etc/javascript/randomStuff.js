// this file just has some random javascript code that I wrote while learning for the first time

// let cleber = {
//     name: 'cleber',
//     age: 30
// }

// let arraylegal = [2,3]
// arraylegal['asd'] = 6
// // console.log(arraylegal);

 let objeto = {
     asd : 2,
     metodo() {
         console.log(this)
         this.name = 'teste'
     },
     funcao : (para, tudo) => para - tudo // arrow functions, used to supply callback functions
}

// let metodinho = objeto.metodo.bind(cleber)
// objeto.metodo()
// metodinho()
// console.log(objeto)
// console.log(cleber)
// console.log(objeto.funcao(2,4))

// const square = (x) => x * x

// console.log(square(2))


testeArray = [1,2,3,4,5]

result = testeArray.map((elem) => elem + 2) // similar to java.stream().map()

const {asd, metodo: mt, funcao} = objeto // object destructuring
console.log(mt)


teste2 = [7,8]

combinado = [...testeArray, 6, ...teste2, 9] // spread operator
console.log(combinado)

const objeto2 = {
    zxc: 3
}

objetoCombinado = {...objeto, qwe: 6, ...objeto2}

console.log(objetoCombinado)


class Animal { // classes
    constructor(species) {
        this.species = species
    }

    move() {
        console.log(this.species + ' is moving.')
    }
}

const dog = new Animal('Canis lupus familliaris')
dog.move()

class Cat extends Animal{ 
    constructor(){
        super('Felis Catus')
    }

    meow() {
        console.log('meowww')
    }
}

const josival = new Cat()
josival.move()
josival.meow()


