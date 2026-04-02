# jubilant-eureka

This is my personal solution to the CODE100 Challange 2026.

The challenge can be read [here](https://puzzles.code100.dev/puzzles/chartsexplosion/)

## how to run the code

- install the dependencies from `requirements.txt`
- run `python .\solve.py` or `python .\solve_and_plot.py` for a graphical output

## how did I solve it

First, I normalized the input values so they all used the same scale.<br/>
Next, I modeled the unknown rectangle as a rotated shape inside the given rectangle, and expressed its width and height as projections on the x- and y‑axes.<br/>
Finally, I set up and solved the resulting linear system to compute the dimensions of the rotated rectangle.<br/>

This is the interactive model I did: 
(made with geogebra)

![rectacle_rotation](https://github.com/user-attachments/assets/21afa200-bd00-477b-916c-6ff3a5376917)

The resulting equation system:

W = w |cos(θ)|+h sin(θ) <br/>
H = w sin(θ)+h |cos(θ)|

where θ in [ 0; π ]

## let's visualize stuff

Using the provided dataset I create a plot of the solution:

<img width="912" height="610" alt="image" src="https://github.com/user-attachments/assets/aad15f9f-e5ca-4c42-a122-07964be34b44" />

In blue the origina normalized rectangles, pink the real rotated bars.

