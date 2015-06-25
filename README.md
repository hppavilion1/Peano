# Peano
An extended implementation of a variant on @rdococ's Table programming language

## Introduction
*Peano* is a semi-esoteric, declarative, map-based programming language comprised entirely of Associative Arrays.

It is named for Giuseppe Peano, an Italian Mathemetician who axiomized arithmetic with his Peano Axioms. Also, he was a founder of Mathematical Logic and Set Theory. Let's just say he had over 200 books and papers. Cool dude.

It is named for him for a few reasons. These include:
* He Axiomized arithmetic. The goal of the Peano language is to have the built-in content as simple as possible, defining even basic operators in external libraries
* Peano (the language), being of a very mathematical sort, would be most appropriately named after a mathemetician. Peano (the person) was just such the mathemetician to name it after
* Peano was a founder of set theory. Sets ≈ Arrays (particularly the sort used in Peano, basically the associative equivalent of ordered sets (that is, unique arrays)).
* Peano is an excellent name for a programming language, and I am yet to encounter one named after him
* He was a pretty cool dude.

It is derived from @rdocooc's original Table programming language, which the author encountered when discussing with rdococ on the
#Esoteric IRC channel on freenode.net. The author read the article and saw its potential, and decided to collaborate with various
other people they met on IRC.

## Code Examples
These are pretty much all taken from the Esolangs page. All credit to the creator, Rdococ
### Booleans
I don't exactly understand these...
```
true: [[]: []],
false: []
```
### Boolean Operations
These demonstrate the powerful form of pattern matching used in Peano. (Booleans are assumed to be imported already)
```
and: [true: [true: true, false: false], false: [true: false, false: false]],
or: [true: [true: true, false: true], false: [true: true, false: false]],
xor: [true: [true: false, false: true], false: [true: true, false: false]],
not: [true: false, false: true]
```

## Links
[The #Estoeric channel on Freenode](http://webchat.freenode.net/?channels=esoteric&uio=d4) (webchat)

[The Specification (perpetual WIP)](https://docs.google.com/document/d/15IhFJ9patZ-CINalHAyDMTxfdwyopGnkiZBtAljBVYY/edit?usp=sharing)

[Table on Esolangs](http://esolangs.org/wiki/Table)

[Giuseppe Peano](https://en.wikipedia.org/wiki/Giuseppe_Peano)

[Peano Axioms](https://en.wikipedia.org/wiki/Peano_axioms)
