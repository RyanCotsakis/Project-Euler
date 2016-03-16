/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

unsigned long largestFactor(unsigned long long n){
	long i = 2;
	while(i <= n/i){
		if(n%i == 0){
			n/=i;
			i=2;
		}
		else
			i++;
	}
	return n;
}
