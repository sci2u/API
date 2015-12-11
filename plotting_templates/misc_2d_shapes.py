import matplotlib.pyplot as plt
import matplotlib.patches as mp


def misc2d(ax):
    """
    Function that uses matplotlib patches to draw common shapes
    The input is a matplotlib ax-object.

    Examples of shapes can be found here:
    http://matplotlib.org/examples/shapes_and_collections/artist_reference.html
    """
    # Simple text which can take latex-expressions and therefore be used to plot symbols.
    ax.text(0.3, 0.7, r'$\otimes A$', fontsize=20)
    # Circle shape which needs: center(x,y), radius.
    ax.add_patch(mp.Circle((0.5,0.5), radius=0.3, color='k', alpha=0.7, fill=False))
    ax.add_patch(mp.Circle((0.5,0.5), radius=0.2, color='r', alpha=0.7))
    ax.add_patch(mp.Circle((0.5,0.5), radius=0.1, color='w', alpha=None))
    # Arrow-shape. Here used to make x-y-axes. There are a lot of different settings, and they need
    # to be tweaked to fit in the frame as only half the arrows on the axes are shown.
    ax.add_patch(mp.FancyArrowPatch((0, 0), (1, 0), 
                                    color='k',
                                    lw=2, 
                                    arrowstyle='-|>',
                                    mutation_scale=20))
    ax.text(1, 0, '$x$', fontsize=20)
    ax.add_patch(mp.FancyArrowPatch((0, 0), (0, 1), 
                                    color='k',
                                    lw=2, 
                                    arrowstyle='-|>',
                                    mutation_scale=20))
    ax.text(0, 1, '$y$', fontsize=20)
    ax.add_patch(mp.FancyArrowPatch((0.5, 0.5), (0.1, 0.1), 
                                    color='b',
                                    lw=2, 
                                    arrowstyle='-|>',
                                    mutation_scale=20))
    # Simple rectangle
    ax.add_patch(mp.Rectangle((0.6, 0.6), 0.2, 0.2, alpha=0.5))

fig = plt.figure()
ax = fig.add_subplot(111)
misc2d(ax)
plt.axis('off')
plt.show()
