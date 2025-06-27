# Space Invaders Game

A classic Space Invaders arcade game implemented in Python using Pygame. Defend Earth by shooting down waves of alien invaders!

## 🎮 Game Overview

This is a faithful recreation of the classic Space Invaders arcade game where you control a spaceship at the bottom of the screen, shooting at rows of descending alien enemies. The game features progressive difficulty, sound effects, and classic arcade gameplay.

## 🚀 Features

- **Classic Gameplay**: Move left/right and shoot at descending enemies
- **Progressive Difficulty**: Each wave increases enemy count and speed
- **Sound Effects**: Laser sounds, explosion effects, and background music
- **Score System**: Earn points for each enemy destroyed
- **Game Over Screen**: Restart or quit options when defeated
- **Collision Detection**: Accurate sprite-based collision system
- **Smooth Controls**: Responsive keyboard input with proper key handling

## 🎯 Game Mechanics

### Player Controls
- **Left Arrow**: Move spaceship left
- **Right Arrow**: Move spaceship right  
- **Spacebar**: Fire laser bullets (up to 3 bullets on screen at once)

### Game Rules
- Destroy all enemies to advance to the next wave
- Each wave spawns more enemies with increased speed
- Game ends if enemies reach the bottom of the screen (y > 440)
- Score increases by 1 point per enemy destroyed

### Progression System
- **Starting Wave**: 4 enemies at speed 3
- **Each New Wave**: +1 enemy, +0.5 speed increase
- **Bullet Limit**: Maximum 3 bullets on screen simultaneously

## 📁 Required Files

The game requires these asset files in the same directory:

### Images
- `player.png` - Player spaceship sprite
- `enemy.png` - Enemy alien sprite  
- `bullet.png` - Laser bullet sprite
- `background.png` - Game background image
- `ufo.png` - Game icon

### Audio
- `laser.wav` - Laser firing sound effect
- `explosion.wav` - Enemy destruction sound
- `background.mp3` - Background music (loops continuously)

## 🛠️ Technical Implementation

### Core Classes

#### Spaceship Class
A versatile sprite class that handles:
- **Player Movement**: Boundary-constrained horizontal movement
- **Enemy Movement**: Horizontal movement with direction changes and downward progression
- **Bullet Movement**: Vertical upward movement for projectiles
- **Collision Detection**: Rectangle-based collision system

### Key Functions

#### `create_enemies(no_of_enemies)`
- Spawns enemies at random positions in the upper portion of the screen
- Ensures enemies don't spawn outside screen boundaries

#### `reset_game()`
- Resets all game variables to initial state
- Recreates player and enemy objects
- Resets score and difficulty parameters

#### `show_game_over()`
- Displays game over screen with restart instructions
- Shows restart (SPACE) and quit (ESC) options

#### `iscollision(bullet, enemy)`
- Handles sprite collision detection using Pygame's `colliderect()` method
- Returns boolean for collision state

#### `show_score(score)`
- Renders and displays current score in top-left corner
- Updates in real-time during gameplay

## 🎨 Game States

### Playing State
- Player can move and shoot
- Enemies move in formation
- Collision detection active
- Score tracking enabled

### Game Over State
- Movement disabled
- Game over screen displayed
- Restart/quit options available
- All game objects frozen

## 🔧 Configuration

### Display Settings
- **Screen Size**: 800x600 pixels
- **Frame Rate**: 60 FPS
- **Background Color**: Black (0,0,0)

### Gameplay Parameters
- **Player Speed**: 5 pixels per frame
- **Initial Enemy Speed**: 3 pixels per frame
- **Bullet Speed**: 7 pixels per frame
- **Enemy Drop Distance**: 60 pixels when hitting screen edge
- **Maximum Bullets**: 3 simultaneous bullets

## 🎵 Audio System

The game features a complete audio system:
- **Mixer Initialization**: Properly initialized before Pygame init
- **Sound Effects**: Laser and explosion sounds with proper timing
- **Background Music**: Continuous looping background music
- **Resource Path Handling**: Compatible with PyInstaller for executable creation

## 🚀 Installation & Setup

### Requirements
```bash
pip install pygame
```

### Running the Game
1. Ensure all asset files are in the game directory
2. Run the Python script:
```bash
python space_invaders.py
```

### Creating Executable
The code includes PyInstaller support with the `resource_path()` function for bundling assets into a standalone executable.

## 🎮 Gameplay Tips

- **Positioning**: Stay mobile to avoid enemy fire patterns
- **Bullet Management**: Use all 3 bullet slots efficiently
- **Wave Strategy**: Clear enemies systematically to prevent overwhelming situations
- **Speed Increases**: Prepare for faster enemies in later waves

## 🔄 Game Loop Structure

The main game loop handles:
1. **Event Processing**: Keyboard input and window events
2. **Game State Updates**: Player/enemy movement and collision detection
3. **Rendering**: Drawing all sprites and UI elements
4. **Display Updates**: Screen refresh at 60 FPS

## 🏆 Scoring System

- **Base Score**: 1 point per enemy destroyed
- **Progressive Waves**: Unlimited waves with increasing difficulty
- **High Score**: Displayed during gameplay in top-left corner

## 🐛 Error Handling

The game includes proper error handling for:
- **Boundary Checking**: Prevents sprites from moving off-screen
- **List Management**: Safe removal of bullets and enemies during iteration
- **Resource Loading**: Proper file path handling for assets

## 📝 Code Structure

The codebase is organized with:
- **Class-based Design**: Reusable Spaceship class for all moving objects
- **Modular Functions**: Separate functions for different game aspects
- **Clean Game Loop**: Well-structured main loop with clear state management
- **Resource Management**: Proper asset loading and cleanup

This Space Invaders implementation provides a complete, playable game experience with all the classic elements that made the original arcade game a timeless classic!
