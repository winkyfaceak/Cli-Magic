#!/bin/bash

# Check if Homebrew is installed, install if we don't have it
if test ! $(which brew); then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

echo "Updating Homebrew..."
brew update

# List of applications to install via Homebrew
brew_apps=(
    git
    gh
    fish
)

# List of cask applications to install
cask_apps=(
    arc
    maccy
    rectangle
    raycast
    linearmouse
    drawio
    gimp
    inkscape
    discord
    windscribe
    steam
    obsidian
    openemu
    transmission
    zed
    goland
    clion
    webstorm
    visual-studio-code
)

# Install Homebrew packages
echo "Installing Homebrew packages..."
for app in "${brew_apps[@]}"; do
    brew install $app
done

# Install cask applications
echo "Installing cask applications..."
for app in "${cask_apps[@]}"; do
    brew install --cask $app
done

echo "Cleaning up..."
brew cleanup

echo "Installation complete!"
