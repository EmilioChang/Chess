# Run from Chess (root) directory
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    if uname -a | grep -qi "MINGW"; then
        python -m Game.GUI.Game
    else
        python3 -m Game.GUI.Game
    fi
fi