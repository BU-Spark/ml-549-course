# CS/DS 549 Spring 2023 HW Neural Net Solution



## Q7 Two-Layer Neural Network

_(Adapted from an exerice from Yan LeCun's Deep Learning Course)_

We have the following two-layer neural network:
$$
\require{ams}
\text{Affine}_1 \rightarrow f \rightarrow \text{Affine}_2 \rightarrow g
$$

Where $\text{Affine}_i  = \textbf{W}^{(i)}\textbf{x} + \textbf{b}^{(i)}$ is the $i$-th affine transformation, $f = \text{ReLU}(\cdot)$ is the Rectified Linear Unit activation function and $g$ is the identity funciton.

When an input $\textbf{x} \in R^n$ is provided to the network,
$\hat{\textbf{y}} \in R^k$ is produced by the network.

To train this network, we choose the MSE loss function
$\ell_{\text{MSE}} (\hat{\textbf{y}}, \textbf{y}) =
|| \hat{\textbf{y}} - \textbf{y} ||^2$, where $\textbf{y}$ is the
desired output.

### Q7.1 Calculate the Forward Pass

For a single input/output data point $(\textbf{x}, \textbf{y})$, 
write down the inputs and outputs for the forward pass of each
layer. You can only use the variables $\textbf{x}$, $\textbf{y}$,
$\textbf{W}^{(1)}$, $\textbf{b}^{(1)}$, $\textbf{W}^{(2)}$ and
$\textbf{b}^{(2)}$ in your answer.

<style>
td, th {
    border: 1px solid grey
}
</style>

#### Q7.1 Solution

We'll use the shorthand $ (\cdot)^+ $ to denote $ \text{max}(\cdot) $ and use subscripts instead of parenthisized
superscripts to denote the $i^\text{th}$ index.

| Layer             | Input                                           | Output                                                          |
|-------------------|-------------------------------------------------|-----------------------------------------------------------------|
| $\text{Affine}_1$ | $\textbf{x}$                                    | $\textbf{W}_1\textbf{x} + \textbf{b}_1$              |
| $f$               | $\textbf{W}_1\textbf{x} + \textbf{b}_1$         | $(\textbf{W}_1\textbf{x} + \textbf{b}_1)^+ $ |
| $\text{Affine}_2$ | $(\textbf{W}_1\textbf{x} + \textbf{b}_1)^+ $ | $\textbf{W}_2 ( (\textbf{W}_1\textbf{x} + \textbf{b}_1)^+ ) + \textbf{b}_2$ |
| $g$               | $\textbf{W}_2 ( (\textbf{W}_1\textbf{x} + \textbf{b}_1)^+ ) + \textbf{b}_2$ | $\textbf{W}_2 ( (\textbf{W}_1\textbf{x} + \textbf{b}_1)^+ ) + \textbf{b}_2$ |
| Loss              | $\textbf{W}_2 ( (\textbf{W}_1\textbf{x} + \textbf{b}_1)^+ ) + \textbf{b}_2$ | $ \|\| \textbf{y} - (\textbf{W}_2 ( (\textbf{W}_1\textbf{x} + \textbf{b}_1)^+ ) + \textbf{b}_2) \|\|^2 $       |


### Q7.3 Backward Pass

Write down the gradient calculated from the backward pass. You can only
use the variables $\textbf{x}$, $\textbf{y}$, $\textbf{W}^{(1)}$, 
$\textbf{b}^{(1)}$, $\textbf{W}^{(2)}$, $\textbf{b}^{(2)}$,
$\frac{\delta \ell}{\delta \hat{\textbf{y}}}$,
$\frac{\delta \textbf{z}_2}{\delta \textbf{z}_1}$ and
$\frac{\delta \hat{\textbf{y}}}{\delta \textbf{z}_3}$ 
 in your answer. The variables $\textbf{z}_1$, $\textbf{z}_2$, 
$\textbf{z}_3$ and $\hat{\textbf{y}}$ are the outputs of 
$\text{Affine}_1$, $f$, $\text{Affine}_2$ and $g$.

#### Q7.3 Solution

It is helpful to draw the tensor/operator graph for this problem to better visualize the chain rule.

![HW1 Tensor Graph](./HW1%20Tensor%20Graph.png)

We use the chain rule to calculate the gradient of the loss with respect to the parameters of the network.

$$
\begin{align}
\frac{\delta \ell}{\delta \textbf{W}^{(2)}} 
   & = \frac{\delta \ell}{\delta \hat{\textbf{y}}} 
      \frac{\delta \hat{\textbf{y}}}{\delta \textbf{z}_3} 
      \frac{\delta \textbf{z}_3}{\delta \textbf{W}^{(2)}}  \\

\frac{\delta \ell}{\delta \textbf{b}^{(2)}} 
   & = \frac{\delta \ell}{\delta \hat{\textbf{y}}} 
      \frac{\delta \hat{\textbf{y}}}{\delta \textbf{z}_3} 
      \frac{\delta \textbf{z}_3}{\delta \textbf{b}^{(2)}} \\

\frac{\delta \ell}{\delta \textbf{W}^{(1)}} 
   & = \frac{\delta \ell}{\delta \hat{\textbf{y}}} 
      \frac{\delta \hat{\textbf{y}}}{\delta \textbf{z}_3} 
      \frac{\delta \textbf{z}_3}{\delta \textbf{z}_2} 
      \frac{\delta \textbf{z}_2}{\delta \textbf{z}_1} 
      \frac{\delta \textbf{z}_1}{\delta \textbf{W}^{(1)}} \\

\frac{\delta \ell}{\delta \textbf{b}^{(1)}} 
   & = \frac{\delta \ell}{\delta \hat{\textbf{y}}} 
      \frac{\delta \hat{\textbf{y}}}{\delta \textbf{z}_3} 
      \frac{\delta \textbf{z}_3}{\delta \textbf{z}_2} 
      \frac{\delta \textbf{z}_2}{\delta \textbf{z}_1} 
      \frac{\delta \textbf{z}_1}{\delta \textbf{b}^{(1)}} \\
\end{align}
$$


| Parameter | Gradient |
|-----------|----------|
| $\textbf{W}^{(1)}$ |  $ \frac{\delta \ell}{\delta \textbf{W}^{(1)}}  = \frac{\delta \ell}{\delta \hat{\textbf{y}}} \frac{\delta \hat{\textbf{y}}}{\delta \textbf{z}_3} \frac{\delta \textbf{z}_3}{\delta \textbf{z}_2} \frac{\delta \textbf{z}_2}{\delta \textbf{z}_1} \frac{\delta \textbf{z}_1}{\delta \textbf{W}^{(1)}} $    |
| $\textbf{b}^{(1)}$ |  $ \frac{\delta \ell}{\delta \textbf{b}^{(1)}} = \frac{\delta \ell}{\delta \hat{\textbf{y}}} \frac{\delta \hat{\textbf{y}}}{\delta \textbf{z}_3} \frac{\delta \textbf{z}_3}{\delta \textbf{z}_2} \frac{\delta \textbf{z}_2}{\delta \textbf{z}_1} \frac{\delta \textbf{z}_1}{\delta \textbf{b}^{(1)}} $    |
| $\textbf{W}^{(2)}$ |  $  \frac{\delta \ell}{\delta \textbf{W}^{(2)}}  = \frac{\delta \ell}{\delta \hat{\textbf{y}}} \frac{\delta \hat{\textbf{y}}}{\delta \textbf{z}_3} \frac{\delta \textbf{z}_3}{\delta \textbf{W}^{(2)}} $    |
| $\textbf{b}^{(2)}$ |  $\frac{\delta \ell}{\delta \textbf{b}^{(2)}}  = \frac{\delta \ell}{\delta \hat{\textbf{y}}} \frac{\delta \hat{\textbf{y}}}{\delta \textbf{z}_3} \frac{\delta \textbf{z}_3}{\delta \textbf{b}^{(2)}} $    |

### Q7.3

Show the elements of $\frac{\delta \textbf{z}_2}{\delta \textbf{z}_1}$,
$\frac{\delta \hat{\textbf{y}}}{\delta \textbf{z}_3}$ and
$\frac{\delta \ell}{\delta \hat{\textbf{y}}}$

### Solution

$$ \textbf{z}_2 
   = \text{ReLU}( \textbf{z}_1 ) 
$$
where ReLU is applied elementwise on $\textbf{z}_1$.

$$
   \textbf{z}_1^{(i)} =
   \begin{cases}
     \textbf{z}_1^{(i)} & \text{if the i-th element } \textbf{z}_1^{(i)} > 0 \\
     0 & \text{otherwise}
   \end{cases}
$$

So the deriviative would be a vector where the i-th element is 1 if $\textbf{z}_1^{(i)} > 0$ and 0 otherwise. We can 
express that somethin like this.
$$
\frac{\delta \textbf{z}_2}{\delta \textbf{z}_1}
= \textbf{I} [\textbf{z}_1 > 0]
$$

Since $g$ is the identity function, we have $\frac{\delta \hat{\textbf{y}}}{\delta \textbf{z}_3} = \textbf{I}$, the identity vector. 

Finally, the derivative of the loss function with respect to $\hat{\textbf{y}}$  
we first expand the loss function as follows.
$$
\begin{align}
 \ell_{\text{MSE}} (\hat{\textbf{y}}, \textbf{y}) & = || \hat{\textbf{y}} - \textbf{y} ||^2 \\
               & = ( \hat{\textbf{y}} - \textbf{y} )^T ( \hat{\textbf{y}} - \textbf{y} ) \\
               & = \hat{\textbf{y}}^T \hat{\textbf{y}} - 2 \hat{\textbf{y}}^T \textbf{y} + \textbf{y}^T \textbf{y}
\end{align}
$$

And then taking the derivative with respect to $\hat{\textbf{y}} $:
$$
\frac{\delta \ell}{\delta \hat{\textbf{y}}} 
= \frac{\delta}{\delta \hat{\textbf{y}}} (\hat{\textbf{y}}^T \hat{\textbf{y}} - 2 \hat{\textbf{y}}^T \textbf{y} + \textbf{y}^T \textbf{y})
=  2 \hat{\textbf{y}} - 2 \textbf{y}
$$

