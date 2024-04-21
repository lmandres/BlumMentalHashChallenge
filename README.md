# BlumMentalHashChallenge
The Blum Mental Hash Challenge is a simple website that tests the robustness of Manuel Blum's Mental Hash described below:

[Mental Cryptography and Good Passwords](https://scilogs.spektrum.de/hlf/mental-cryptography-and-good-passwords/)

However, Rob Shearer has shown that Manuel Blum's Mental Hash is cryptographically weak as demonstrated by a naive attack with about 150 characters of ciphertext:

[The "Blum Mental Hash" Is A Lousy Idea](https://v.cx/2022/05/blum-mental-hash)

Despite this, the ciphertext (i.e. the password) is not supposed to be made public.  So, my question is, how easy is it to recover the Mental Hash keys if the hash is used as a password generator for different sites?

## Directions
The Blum Mental Hash Challenge is hosted at:

[https://blum-mental-hash-challenge.ue.r.appspot.com/login](https://blum-mental-hash-challenge.ue.r.appspot.com/login)

Try to get into the Authenticated page.  If you are able to do this, post the following in the issues for this repository:

* Login
* Password
* Digit sequence
* Alphanumeric mapping