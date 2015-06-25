# Peano
An extended implementation of a variant on @rdococ's Table programming language

## Introduction
*Peano* is a semi-esoteric, declarative, map-based programming language comprised entirely of Associative Arrays.

It is named for Giuseppe Peano, an Italian Mathemetician who axiomized arithmetic with his Peano Axioms

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
These demonstrate the powerful form of pattern matching used in Peano. 
```
and: [true: [true: true, false: false], false: [true: false, false: false]],
or: [true: [true: true, false: true], false: [true: true, false: false]],
xor: [true: [true: false, false: true], false: [true: true, false: false]],
not: [true: false, false: true]
```

## Links
[http://webchat.freenode.net/?channels=esoteric&uio=d4](The #Estoeric channel on Freenode) (webchat)

[https://docs.google.com/document/d/15IhFJ9patZ-CINalHAyDMTxfdwyopGnkiZBtAljBVYY/edit?usp=sharing](The Specification (perpetual WIP))

[http://esolangs.org/wiki/Table](Table on Esolangs)

[https://en.wikipedia.org/wiki/Giuseppe_Peano](Giuseppe Peano)

[https://en.wikipedia.org/wiki/Peano_axioms](Peano Axioms)
