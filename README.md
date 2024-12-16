# predicting-java-prng
Finding future outputs of pseudo-random number generator of Java's Random class given first two outputs

Information:

Assume we don't know the seed inputted to the constructor of Java's Random class.

```
long secret_seed = //Unknown value
Random rand = new Random ( secret_seed );
int n1 = rand.nextInt();
int n2 = rand.nextInt();
int n3 = rand.nextInt();
```

Given the first two outputs of Random.nextInt():
 - n1: -745632980
 - n2: 2066963502

We are going to find the value of n3.


