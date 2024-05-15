# [PART 2] Implementing SplitScreen Multiplayer in Godot 4, a tutorial and reflection on the journey

- [\[PART 2\] Implementing SplitScreen Multiplayer in Godot 4, a tutorial and reflection on the journey](#part-2-implementing-splitscreen-multiplayer-in-godot-4-a-tutorial-and-reflection-on-the-journey)
  - [Multi-Player](#multi-player)
    - [Defining Actions](#defining-actions)
    - [Abstracting Actions even further](#abstracting-actions-even-further)
    - [Consuming Actions](#consuming-actions)
  - [Conclusion](#conclusion)

In the [last part](https://www.blessedsleepseeker.com/blog/split-screen-multiplayer-part1), we've seen how I managed to create a modular split-screen and letting all players be in the same world. We're now gonna see how I managed to instance the same *player scene* in every `SubViewport` and still have each *real player* be able to play the game.

## Multi-Player

My solution takes advantage of various features of Godot or GDScript.

The first one is [**Actions**](https://docs.godotengine.org/en/stable/tutorials/inputs/input_examples.html). Actions allow us to abstract specific in-game actions like going left, jumping or shooting, making them decoupled from the actual keyboard or controller input. Once defined, an action can be checked with the help of the [Input](https://docs.godotengine.org/en/stable/classes/class_input.html) singleton.

The second feature is [**Format Strings**](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_format_string.html), also known as *string interpolation* in other languages.

The third feature is... **Variables** ?? Uhh ?? (Amazing reveal tbh)

Ok, let's jump right in !

### Defining Actions

Directly in the godot action panel, you are going to create actions for all of your players. You should follow a pattern of your choosing. Mine was first put `p`, then the player number, for example 1, followed by an underscore and the name of the action. For player 1, I created 5 actions : `p1_up`, `p1_down`, `p1_left`, `p1_right`, `p1_attack`. For player 2, the actions are `p2_up`, `p2_down`, `p2_left`, `p2_right`, `p2_attack` and so on...

![godot action panel](https://docs.godotengine.org/en/stable/_images/07.input_map_tab.png)

I personnaly do this dynamically at runtime because I hate hardcoding things but this is beyond the scope of this tutorial. TLDR : Once I know how much players are in the game, I check if all actions for each players are created and have inputs set to them, and if not, I display a prompt to the user waiting for their input and save it.

You can find more infos on how I did it [here](https://github.com/BlessedSleepSeeker/CarrotsOfChaos/blob/main/game/autoloads/inputhandler.gd) and [there](https://github.com/BlessedSleepSeeker/CarrotsOfChaos/blob/main/game/Scenes/Menu/settings/StartGameSettings.gd).

### Abstracting Actions even further

My player use a finite *state-machine* with a script dedicated to each state, but the inputs declarations are centralised in my player script. As with part one, I will shorten, cut and change my code as needed to make it simpler to understand.

Let's keep in mind that each player get his `PLAYER_NBR` set right at instanciation with the right number. The player in the top left is player 1.

```swift
class_name Player
extends CharacterBody2D

var PLAYER_NBR: int = 1

var act_left: String = "p%d_left" % PLAYER_NBR
var act_right: String = "p%d_right" % PLAYER_NBR
var act_up: String = "p%d_up" % PLAYER_NBR
var act_down: String = "p%d_down" % PLAYER_NBR
var act_attack: String = "p%d_attack" % PLAYER_NBR

func reassignControls() -> void:
    act_left = "p%d_left" % PLAYER_NBR
    act_right = "p%d_right" % PLAYER_NBR
    act_up = "p%d_up" % PLAYER_NBR
    act_down = "p%d_down" % PLAYER_NBR
    act_attack = "p%d_attack" % PLAYER_NBR
```

We start by defining variables to store our actions names for each possible different input. I have only five actions, one for each cardinal directions, and one for attacking, but you could make more. Let's look at the right part of each declarations.

`"p%d_left" % PLAYER_NBR` is the [**Format Strings**](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_format_string.html) I've talked about at the beginning, and this is were all the magic happen. With format string, you can simply add a `%` followed by a few specific letters (read the docs) and then replace both by another variable or constant. In our case, we want to add a number, so we add ``%d`` right after the `p`.  
Let's manually resolve this operation ! First, resolve `PLAYER_NBR`. Since `PLAYER_NBR` is set as one, we can write our operation like this : `"p%d_left" % 1`. Now let's format our string, replacing `%d` with the value after `%` : `p1_left`. And that's it ! Remember our defined actions ? Now we have created a string variable with a defined action name inside.

The function `reassignControls()` is doing the same thing, and should be called when the `PLAYER_NBR` is changed.

### Consuming Actions

```swift
func handle_input(_event: InputEvent) -> void:
  player.v_direction = Input.get_axis(player.act_left, player.act_right)
  if Input.is_action_just_pressed(player.act_up):
    state_machine.transition_to("JumpSquat")
  if Input.is_action_just_pressed(player.act_attack):
    state_machine.transition_to("Attack")
```

Now that we have dedicated variables holding actions names, we simply can pass this to our input handling function.

My state machine is the one responsible for passing input data to the current state, so I have few reference to state.  
There isn't much to do : instead of using `Input.is_action_pressed("p1_up")`, I simply pass `player.act_up` and I am done.

## Conclusion

As you can see, this part is very quick and not too complex. Abstracting actions with an additional holder variable is very quick, easy and imo should be done even if you do not think you're going to implement multiplayer.  
Imagine that you have a state machine with say, 20 differents states and that your player actions needs to be renamed. If you do not have implemented abstraction, this mean a lot of boring work of find + replace. If you have abstracted actions, this is simply a one time change in your player script for each actions.

I hope you liked this second part ! Bye :)