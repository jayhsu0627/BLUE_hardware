# Python Scripts Definition

## G29 Overview
see 

![G29](/pic/G29.jpg)

## Message Definition

|  **Steering Wheel** |         |
| ----          | ----          |
|  Position:    | 1-2nd Bytes   |
|  Value:       | [0-65535]     |
|  Type:        | EV_ABS        |
|  Name:        | 'ABS_X'       |
|  **Throttle** |               |
| ----          | ----          |
|  Position:    | 3rd Bytes     |
|  Value:       | [0-255]       |
|  Type:        | EV_ABS        |
|  Name:        | 'ABS_Z'       |
|  **Brake**    |               |
| ----          | ----          |
|  Position:    | 4th Bytes     |
|  Value:       | [0-255]       |
|  Type:        | EV_ABS        |
|  Name:        | 'ABS_RZ'      |
|  **Clutch**   |               |
| ----          | ----          |
|  Position:    | 5th Bytes     |
|  Value:       | [0-255]       |
|  Type:        | EV_ABS        |
|  Name:        | 'ABS_Y'       |


|  **L2**       |               |
| ----          | ----          |
|  Position:    | with R2 @(5,0)|
|  Value:       | [0,1]         |
|  Type:        | EV_KEY        |
|  Name:        | 'BTN_BASE2'   |
|  **R2**       |               |
| ----          | ----          |
|  Position:    | with L2 @(5,0)|
|  Value:       | [0,1]         |
|  Type:        | EV_KEY        |
|  Name:        | 'BTN_BASE2'   |

## Matrix

|   |0     |  1    | 2     | 3     | 4     |  5    |  6    | 7   |
| :-: | :-:| :-:   | :-:   | :-:   | :-:   | :-:   | :-:   | :-: |
| 0 |\|<----| ---- | ---- | **Steering Wheel** | ----  | ----  | ---- | ----|
| 1 | ----  | ---- | ---- |    ----| ----  | ----  | ---- | <----\||
| 2 |\|<----| ---- | ---- | **Throttle** | ----  | ---- |----|<----\||
| 3 |\|<----| ---- | ---- | **Brake**   | ----  | ----  |---- | <----\||
| 4 |\|<----| ---- | ---- | **Clutch** | ----  | ----  |---- | <----\||
| 5 |Set_Zero^\*|       |      |      |      |      |      |      |
| 6 |      |       |      |      |      |      |      |      |
| 7 |      |       |      |      |      |      |      |      |

* Set_Zero activate only when press L2 and R2 simultaneously.
