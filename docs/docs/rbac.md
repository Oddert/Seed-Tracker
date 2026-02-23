# Resource Based Access Control

[View on live editor](https://www.mermaidchart.com/play#pako:eNqVlV1vgjAUhv9K426HiS3ugiVLmGIk0WniFpfALjoo0oiF0G5uWfbfp3xZ0A7hqu15es77Nqflp-fFPukZPU3TXObFLKAbw2UAiJDsiAF8nG5dlgWDKN57IU7FMQwA_3jfpDgJgRlF4BGzLViOJmCVYI_wnDh--xALGgyc9dR8tidvp0BCvZgMnKU9WljN5YCyIjKxn6QgIT6nA8eyxitbWsbUJ4cNpj22ZHpHdjhKQjxw5tbcnC2nppxKeE6_3y9WCPMbpl44STlYzV4Bjg6-zx0Bra89FBOospdD2RiqrUrUYQovOc8t5mA2hmq7OVVOYdP9Za8gxBxgT9BPLIjfEAklhUjpA9Z9IKUPKPlANR_n2tZYeGFEuQALRho1kVRQV8pCdVm6UhaSZOlXy3rex601h1fVHJ7XdBkX3xGpeo6LNN4S4yYI0G0-1vbUF6GhJ1_3dRi2wSVedGpJIxSoUxfdcD2LOrB6G1ujs4tTWUSoJXnWn51w1A3Xu-HDNrzcUNz86mgCXZ28uF3Xs6gDq3dgh21sSZ8ereo47v45vepRa8PLDfkfQ1JzobF6v395rUqe)

```mermaid
---
config:
  theme: dark
---
flowchart
    subgraph All Bank PCF Spaces
        whatif1[WHATIF]
        picoe1[PICOE]
        picoefin1[PICOEFIN]
        eedsi1[EEDSI]
        aiden1[AIDEN]
        memalpha1[MEMALPHA]
        etc[...]
    end
    subgraph Users SLX allows
        whatif1 -.-> whatif2[WHATIF]
        picoe1 -.-> picoe2[PICOE]
        picoefin1 -.-> picoefin2[PICOEFIN]
        aiden1 -.-> aiden2[AIDEN]
        memalpha1 -.-> memalpha2[MEMALPHA]
    end
    subgraph User has activated
        picoe2 -.-> picoe3[PICOE]
        picoefin2 -.-> picoefin3[PICOEFIN]
        aiden2 -.-> aiden3[AIDEN]
    end
    subgraph Watchlist One
        picoe3 -.-> picoe4[PICOE]
        picoefin3 -.-> picoefin4[PICOEFIN]
        aiden3 -.-> aiden4[AIDEN]
    end
    subgraph Watchlist Two
        picoefin3 -.-> picoefin5[PICOEFIN]
        aiden3 -.-> aiden5[AIDEN]
    end

style whatif1 stroke:#ff3,stroke-width:4px;
style whatif2 stroke:#ff3,stroke-width:4px;

style picoe1 stroke:#33f,stroke-width:4px;
style picoe2 stroke:#33f,stroke-width:4px;
style picoe3 stroke:#33f,stroke-width:4px;
style picoe4 stroke:#33f,stroke-width:4px;

style picoefin1 stroke:#f33,stroke-width:4px;
style picoefin2 stroke:#f33,stroke-width:4px;
style picoefin3 stroke:#f33,stroke-width:4px;
style picoefin4 stroke:#f33,stroke-width:4px;
style picoefin5 stroke:#f33,stroke-width:4px;

style aiden1 stroke:#3f4,stroke-width:4px;
style aiden2 stroke:#3f4,stroke-width:4px;
style aiden3 stroke:#3f4,stroke-width:4px;
style aiden4 stroke:#3f4,stroke-width:4px;
style aiden5 stroke:#3f4,stroke-width:4px;

style memalpha1 stroke:#f63,stroke-width:4px;
style memalpha2 stroke:#f63,stroke-width:4px;

style eedsi1 stroke:#3ff,stroke-width:4px;
```
