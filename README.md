# cs331assign4
Next steps:<br>
1. Calculate probabilities for every feature for classLabel = 0 and classLabel = 1.
    b.
       P(word = 1 | positive) =
          (word.count.positive+1)/(sentence.count.positive+2)
       P(word = 0 | postivie) =
          (sentence.count.positive-word.count.positive+1)/(sentence.count.positive+2)
2. Encode logic to choose which probabilities to access from vectors.
3. Calculate and compare classification probabilities, make classification.
4. Perform classification on training and testing sets to determine baseline performance benchmark.
5. Fine-tune classification mathematics via log space calculations (removes numerical instability) and uniform Dirichlet priors (counteract zero counts).
6. Modify input filtering to ignore common grammatical articles, number junk, etc. - then retest for performance.
