# Bioinformatics
Example of completed bioinformatics assignment.
Can use to find the highest scoring random motifs by running N times. 

A rather complicated example of the work assigned in a beginners bioinformatics class on Coursera.  

Definition of bioinformatics: "the science of collecting and analyzing complex biological data such as genetic codes"  

Code definitions:
* k or k-mer: substring within DNA string
* motif: pattern that appears at least once in each of several regions of DNA
* motif matrix: list of strings Motifs
* Score(Motifs): number of unpopular letters in motif matrix, the goal is to minimize the score for the most conserved matrix
* pseudocounts: add an amount to each column of the matrix to prevent probailities from becoming 0.
* profile matrix: frequency of i-th nucleotide in j-th column of motif matrix, divide by number of rows
* pr: probabilities
* consensus string: Consensus(Motifs), returns string of most popular nucleotides in each column
* count: number of times each k-mer substring appears in DNA string
* M: best motif
* RandomizedMotifSearch: randomly select the initial collection of k-mers that form motif matrix

In the course, we analyzed example strings of DNA including ATCG nucleotides. Currently, the DNA, k-mer length, and number of times to repeat is hard-coded, so no input is taken from a user.  

The output of the code tells the user:
* The randomized motifs: selected from the original DNA string of chosen length 8
* M: best motif
* Profile matrix: probabilites of each nucleotide per column of the motif matrix
* Probable motifs: motifs with the highest overall probabilities
* Highest scoring motifs: motifs that create the highest score
* Score: the score of the above highest scoring motifs

To-dos:
* Take in user input of DNA strings, k-mer length, and number of times to repeat analysis
* Add comments to explain what the heck is going on
* Add additional analysis and manipulation of the DNA
