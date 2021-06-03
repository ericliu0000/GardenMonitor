# GardenMonitor

#### Alex McLellan, Wujin Ju, Eric Liu

A program intended to run on a small single board computer that deploys a web interface to the local network to facilitate watering and plant monitoring. It presently uses Flask and some vendor libraries, and is not in a tested state.

### Running

You may download a .zip file, and just run `main.py` in the `website/` directory. Requirements are in the source files.

### Notes

* Flask is blocking, so we had to try to thread the program
* The project might have gone better with another language, like JavaScript
* Within this class, it is impossible to make a usable project:
  * There is insufficient time for engineering a solution unless a member does not program
  * There are insufficient resources for doing this online
