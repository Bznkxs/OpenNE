# Experiment Settings

Description of OpenNE/src/exps/settings.json

## Target

This json file (settings.json) aims to provide a clear and detailed description of our experiment settings. We shall put all our experiment **variables** and **options** in this file.

### Fields

Each part enclosed by braces (`{` and `}`) are referred as fields.

Each field except for the root field is named by the string just before its starting brace.

We can further divide the **models** field into several sub-fields, eg. **encoders**, **decoders**, etc.

### Variables

Variables are components of a certain **field**. As for our experiment setting field (the outermost field), our main variables are **tasks**, **datasets**, **models**. Our root field can also be seen as a variable.

When considering variables of some field that describes variable *v*, we refer to *v* as an **attribute**.

### Options

Values you can choose for variables. For example, we have options **node_classification** and **graph_classification** for variable **tasks**.

### Relations between Variables and Options

In each experiment, we choose **exactly one option** from **each variable**.

## Format

In each **variable field**, we mark each variable as a dict item:

```json
{ // some variable field
    "variable1": { / ... / },
    "variable2": { / ... / }
    // ... 
}
```

We mark the options for the variable as an item, `'_options'`:

```json
{ // some variable field
    "variable1": { / ... / },
    "variable2": { / ... / },
    "_options": { / ... / } 
}
```

In each **option field**, we divide options into several **option groups** where we describe each option in lists:

```json
{ // some option field
    "classification": ["option1", "option2"],
    "regression": ["option3", "option4"]
}
```
### Option Generation

For fields with variables, we describe the option field using **the option generation rule**, as described below:

- Each option generation rule is a **field** and should be seen as **an option group**:

  ```json
  { // some option field
      "classification": ["option1", "option2"],
      "rule1": { / rule field / }
  }
  ```

- Each rule lists all variables of a certain attribute and selected groups of options. The rule is equivalent to the descartes product of all selections.

  For example:

  ```json
  {
      "var1": {"_options": {"group1A": [0, 1], "group1B": [0, 2]}},
      "var2": {"_options": {"group2A": ["a", "b"]}},
      "_options": {
          "A": {"var1": ["group1A"], "var2": ["group2A"]}
      }
  }
  ```

  means

  ```json
  {
      "_options": {
          "A": [{"var1": 0, "var2": "a"},
                {"var1": 0, "var2": "b"},
                {"var1": 1, "var2": "a"},
                {"var1": 1, "var2": "b"},
               ]
      }
  }
  ```

- Full selection of all options in one variable can be simplified as "all". Note that duplicated options will be removed:

  ```json
  {
      "var1": {"_options": {"group1A": [0, 1], "group1B": [0, 2]}},
      "var2": {"_options": {"group2A": ["a", "b"]}},
      "_options": {
          "A": {"var1": "all", "var2": "all"}
      }
  }
  ```

  Thus option group A has 3*2=6 options.

- "all" is used by default (can omit)

- Can describe option group using other keywords.

