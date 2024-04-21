# Implementing SplitScreen Multiplayer in Godot 4, a tutorial and reflection on the journey

[DISCLAIMER] This is part one of a two-parter ! I will only cover the actual split-screen here, and will talk about controlling the players in the second part !

- [Implementing SplitScreen Multiplayer in Godot 4, a tutorial and reflection on the journey](#implementing-splitscreen-multiplayer-in-godot-4-a-tutorial-and-reflection-on-the-journey)
  - [The Epic Split(Screen)](#the-epic-splitscreen)
    - [What we want to achieve](#what-we-want-to-achieve)
    - [Implementation In Godot](#implementation-in-godot)
      - [SubViewportContainer \& SubViewport](#subviewportcontainer--subviewport)
      - [GridContainer](#gridcontainer)
        - [Columns](#columns)
        - [Split Screen Building Algorithm](#split-screen-building-algorithm)
    - [Split-Screen Conclusion and Going Further](#split-screen-conclusion-and-going-further)
  - [Part One Conclusion](#part-one-conclusion)

Well, well, well... What a long title. For Carrots of Chaos, I had to develop a split-screen multiplayer system which would have a variable number of player between 1 and 8. The limit being put to 8 because you will not see anything if you add more players. Let's talk about how I handled both the spliting screen dynamically, the many player controls needed to control 8 of them, what's worked, what could have been improved and more !

## The Epic Split(Screen)

### What we want to achieve

A split-screen game usually requires a few things :

> Each player has its own physical screen space.

![Mario Kart 4 Player Split](https://www.blessedsleepseeker.com/static/base/blog_articles/split_screen/mariokartsplitscreen.png)

Well yeah, kinda obvious, it's called split-screen, because we split the physical screen... If we have 1 player, we do not split the screen. If we have 2 players, we will split the physical space in 2, if we have 3 players, we will split it in... 4 ??? What ?  
This is for competitive integrity. If a player has a bigger space of the screen, he has an advantage over the others and I didn't want that, despite my game being hyper chaotic and not really competitive. Either way, I didn't want some players to feel like they got screwed cause they couldn't see as far as another lucky player. Althought, the idea of screwing players up on purpose by growing or shrinking their physical space on the screen in a coop game is funny... I'll write it down somewhere.  
Also, this leads to a specific case that each split-screen game handle differently. What are we doing with this empty space if there isn't an even number of players ? In my case, I decided to leave it empty because gamejam time restriction are tight.

![3 players split in Carrot of Chaos](https://www.blessedsleepseeker.com/static/base/blog_articles/split_screen/3player_split.png)

> Each physical player's screen space should follow a specific player.

Imagine you are going to a friend house to play Mario Kart 64, plug in your controller, pick up your favorite driver, and then... you have to drive using the minimap on player 1 screen because both split-screen follow player 1 ??? This doesn't make any sense (which is why you've never seen this), each player should have its own camera following them and being displayed in their physical screen space.

> Players should be able to interact and play on the same level, but also the opposite might true, fuck ???

Most splitscreen games are about interacting with your friends and doing silly things together. But some are about finishing a dedicated task in a separate level the fastest or whatever that make them in different levels. Either way, we want our system to be able to handle both situations.  
For my games, I wanted my players to interact and be on the same level, so this is what I am going to talk about.

> Rules are made to be broken (once you've understood why they exist)

This is what the basic implementation of split-screen should do. I am purposely leaving out a lot of fancy things that play with theses "rules", like the ability to swap to other players POV once you've finished a specific task, for simplicity sake, and also because I'm very lazy.

### Implementation In Godot

It's gamedev time !

Same World Split-Screen in Godot 4 is quite simple :

1. Create a [``GridContainer``](https://docs.godotengine.org/en/stable/classes/class_gridcontainer.html) and set the Anchor Preset to `Full Rect`.
   1. Tweak `GridContainer.columns`.
   2. Tweak the ``GridContainer``'s theme's parameters to adjust spacing to your liking.
2. Add X [``SubViewportContainer``](https://docs.godotengine.org/en/stable/classes/class_subviewportcontainer.html#class-subviewportcontainer) with each a [``SubViewport``](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport) as a child.
3. Add your level scene as a child of the first `SubViewport`.
4. Inside each `SubViewport`, add a player with a camera attached and active.
5. Set each `SubViewport.world_2d` to be the same as the one who host the level.

That's it ! End of the talk, wrap it up boys, we had a good run. What ? Actually details how to do this ? Ok sure...

#### SubViewportContainer & SubViewport

We will start by handling one player's own space !  
I created a new scene with a `SubViewportContainer` as parent, a `SubViewport` and a `MarginContainer` as child. I then added a script to the `SubViewportContainer`, naming my new class `PlayerViewport`.

![SubViewportContainer scene](https://www.blessedsleepseeker.com/static/base/blog_articles/split_screen/subviewportcontainer.png)

The [``SubViewportContainer``](https://docs.godotengine.org/en/stable/classes/class_subviewportcontainer.html#class-subviewportcontainer) is a control node (useful for automatic resizing and being manipulated by other controls !), which is used to host a `SubViewport` as a child.

The [`MarginContainer`](https://docs.godotengine.org/en/stable/classes/class_margincontainer.html) (promptly renamed M in my scene) is used to house all my UI element that every player should have on their own screen space. Think HP, Score, speed or bullets left...

The [``SubViewport``](https://docs.godotengine.org/en/stable/classes/class_subviewport.html#class-subviewport) is just here because this is the node that actually draw things. I tweaked a few options because my game is pixel-art and I wanted a transparent bg, but you shouldn't have to change anything.

The script is more interesting. I removed both the Parallax stuff that should be here, and the Player's UI stuff that shouldn't be here, it should be handled by a script in the `MarginContainer`.

```swift
class_name PlayerViewport
extends SubViewportContainer

@export var PLAYER_NBR: int = 1
@export var player_scene = preload("res://scenes/Character/Player.tscn")
@onready var viewport: Viewport = $SubViewport

var player: Player

func set_player_nbr(nbr: int) -> void:
    PLAYER_NBR = nbr
    var instance: Player = player_scene.instantiate()
    instance.PLAYER_NBR = PLAYER_NBR
    player = instance
    viewport.add_child(instance)
    this_is_where_i_connect_my_player_to_ui()
    this_is_where_i_update_my_ui_with_player_info()

func set_level(level: Level) -> World2D:
    viewport.add_child(level)
    return viewport.world_2d

func set_world(world: World2D) -> void:
    viewport.world_2d = world
    this_is_where_i_instantiate_and_add_the_parallax()
```

Let's go over everything slowly :

```swift
class_name PlayerViewport
extends SubViewportContainer

@export var PLAYER_NBR: int = 1
@export var player_scene = preload("res://scenes/Character/Player.tscn")
@onready var viewport: Viewport = $SubViewport

var player: Player
```

Here, I declare a bunch of variables and links to scene I will instantiate later with ``preload()``.  
The `PLAYER_NBR` is used to know which player is housed inside this viewport and to pass this information to the player (we will use this for control assignement later).
The ``player_scene`` and `parallax_BG` are preloaded, and will be used once we set up our game.
The `player` var is here to store our player. It is stored mostly for UI signals (which shouldn't be in this script).

```swift
func set_player_nbr(nbr: int) -> void:
    PLAYER_NBR = nbr
    var instance: Player = player_scene.instantiate()
    instance.PLAYER_NBR = PLAYER_NBR
    player = instance
    viewport.add_child(instance)
    this_is_where_i_connect_my_player_to_ui()
    this_is_where_i_update_my_ui_with_player_info()
```

`set_player_nbr()` is essentially a constructor. It is called once by the script building the split-screen. It will instantiate my player, set its player number, store it then add it to the scene. I then connect and update the UI here even tho I should do it elsewere...

```swift
func set_level(level: Level) -> World2D:
    viewport.add_child(level)
    return viewport.world_2d

func set_world(world: World2D) -> void:
    viewport.world_2d = world
    this_is_where_i_instantiate_and_add_the_parallax()
```

`set_level()` is used to host the actual level geometry. This function is called only on the player 1's viewport. It return a ``World2D`` object that will be passed to other `PlayerViewport.set_world()` functions.  
`set_world()` simply take the `World2D` and set it as their own `SubViewport.world_2d`. This function is called on every `PlayerViewport` except the first one.  
This process ensure that the players added in the previous step are actually existing in the same universe and can interact together !

#### GridContainer

Now that we have a space for every players, let's put them next to each others with our ``GridContainer`` !  
I've choosen to use a [``GridContainer``](https://docs.godotengine.org/en/stable/classes/class_gridcontainer.html) for a few reasons :

- It's a control node with all the benefits they have (automatic resizing via anchoring for the control childs of the GC).
- It will split each space evently (remember competitive integrity ?).
- Columns handling for more than 4 players is really easy.

Let's look at the `setup()` function, which is responsible for handling the instatiation of our `PlayerViewport`s.

```swift
class_name WorldHandler
extends Node

@export var playerViewportScene = preload("res://scenes/game_world/PlayerViewport.tscn")
@onready var splitGrid: GridContainer = $SplitGrid

@export var player_count: int = 0
@onready var players: Array = []

var level: Level

func setup():
    splitGrid.columns = (player_count / 2) + player_count % 2

    var levelWorld: World2D = null
    for i in range(0, player_count):
        var playerViewport: PlayerViewport = null
        playerViewport = playerViewportScene.instantiate()
        splitGrid.add_child(playerViewport)
        if i == 0:
            level = levelScene.instantiate()
            levelWorld = playerViewport.set_level(level)
        else:
            playerViewport.set_world(levelWorld)
        playerViewport.set_player_nbr(i + 1)
        players.append(playerViewport.get_player())
```

##### Columns

Here is my code that decide the number of columns the grid should have depending on player :

```swift
splitGrid.columns = (player_count / 2) + player_count % 2
```

For ``GridContainer.columns``, 1 means that every player's space will be on a single column, 2 or more will add columns, making lines (confusing) of players, i don't know how to explain it better just press the button and see for yourself.

The logic behind is just "add a column for every 2 players after the first one". So if we have 3 players, `(3 / 2) + 3 % 2 = 1 + 1 = 2`.  
`3 / 2 = 1` is because we are using ``int`` for our maths, and in Godot if you divide ``int``, the engine just discard the decimal.

For the theme's parameters, I didn't change spacing at all, but you could add a divide to visually "split" the screen. Theming is an entire feature which I will not cover here, you can just change the property by overriding them in the editor !

![GridContainer Editor Settings](https://www.blessedsleepseeker.com/static/base/blog_articles/split_screen/gridcontainer.png)

##### Split Screen Building Algorithm

```swift
var levelWorld: World2D = null
for i in range(0, player_count):
    var playerViewport: PlayerViewport = null
    playerViewport = playerViewportScene.instantiate()
    splitGrid.add_child(playerViewport)
    if i == 0:
        level = levelScene.instantiate()
        levelWorld = playerViewport.set_level(level)
    else:
        playerViewport.set_world(levelWorld)
    playerViewport.set_player_nbr(i + 1)
    players.append(playerViewport.get_player())
```

We start by creating a `World2D` variable and set it to null.  
`for i in range(0, player_count)` : Loop the instantiation for every players.  
Do you remember which `PlayerViewport` function we should call to store it ? It's `set_level()`. And then we will pass it to `PlayerViewport.set_world()` to synchronise our viewport 2D worlds. Pay attention to the fact that `levelScene` (which is actually my level handler, doing a lot more than being 2D geometry), is only instantiated once, `if i == 0:`. Once we go to the second player, we simply have to call `PlayerViewport.set_world()` instead !  
Afterwards, I set the player number inside our `PlayerViewport` with i + 1 (because we start our for loop at 0), and append our player to an of players. I use this array for various things, like setting a spawnpoint in my level, my chaos modifiers which can shuffle things around, or checking if a player is the last one alive.

### Split-Screen Conclusion and Going Further

That's it for the Split-Screen implementation ! As I said previously, this is only a basic implementation with holes and issues. We did not cover topics like what to do with the free space we have or how could you dynamically resize the `SubViewport` to troll your players.  
For a gamejam game, though, it was good enough for me, and it still is.

I think design space for split-screen exist and that we could push and play with the concept further still ! Carrots of Chaos has a "chaos" system, designed to create variance and random event, and I thought of a chaos effect that would shuffle the players's screenspace around or change it's form from a rectangle to a circle... Countless ideas exist !

I also will repeat that my code has been cleaned and that I removed a lot of superfluous things here like the UI signals connections. You'll have to figure this for yourselves !

## Part One Conclusion

Thank you for reading up until this point ! This is part one of 2, and the subject of the second part will be dedicated to our players controls ! I have only one player scene and needed each instanted one to be properly controllable by each player.

I hope you've enjoyed your time with me, and I'll see you in part 2 !
