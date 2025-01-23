# NetworkOptimizationCPN
A Colored Petri Net (CPN) model for simulating and optimizing the routing of a potential organization's network, comprising three remote sub-networks. Includes hierarchical modeling and path optimization to identify efficient communication routes.

## Local setup & dependencies
### venv
This repository is using Python's venv: https://docs.python.org/3/library/venv.html

With venv, a virtual invironment is created & all of the dependencies are installed inside this environment, instead of your local environment.

### Essentials
All the dependencies are located to the file requirements.txt & you can easily install them. The steps ar located in the next section.

So, you'll only need locally Python.

Make sure you'll get the latest version (v3.13.1): https://www.python.org/downloads/

### Dependencies Installation

Create a Virtual Environment: This creates a folder named venv where all your dependencies will be installed:

```bash
python3 -m venv venv
```

Activate the Virtual Environment:

- linux / mac
```bash
source venv/bin/activate
```

- Windows
```bash
venv\Scripts\activate
```

When activated, your terminal prompt will change to something like:

```bash
(venv) $
```

Finally, install dependencies:

```bash
pip install -r requirements.txt
```

In order to add a new dependency:

Activate the Virtual Environment & run

```bash
pip install <package_name>
```
```bash
pip freeze > requirements.txt
```

When you're done working, deactivate the virtual environment with:

```bash
deactivate
```