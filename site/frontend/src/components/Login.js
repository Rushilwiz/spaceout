import React, {Component} from 'react';
import {
    Button,
    FormControl,
    FormControlLabel,
    FormHelperText,
    Grid, Link,
    Radio,
    RadioGroup,
    TextField,
    Typography
} from "@material-ui/core";

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            password: ''
        }
    }

    usernameChanged = (e) => {
        this.setState({
           username: e.target.value
        });
    }

    passwordChanged = (e) => {
        this.setState({
            password: e.target.value
        });
    }

    loginPressed = () => {
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            username: this.state.username,
            password: this.state.password,
          }),
        };
        fetch("/api/auth/token/login", requestOptions)
          .then((response) => {console.log(response); return response.json();})
          .then((data) => console.log(data));
    }

    render() {
        return (
            <div style={{ minHeight: '100vh', minWidth: '100vw' }}>
              <Grid container spacing={3} direction="column" alignItems="center" justify="center">
                <Grid item xs={12} align="center">
                  <Typography component="h3" variant="h3">
                    Login
                  </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                  <FormControl component="fieldset">
                    <FormHelperText>
                      <div align="center">Username</div>
                    </FormHelperText>
                    <TextField
                      required={true}
                      type="username"
                      inputProps={{
                        min: 1,
                        style: { textAlign: "center" },
                      }}
                      onChange={this.usernameChanged}
                    />
                  </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                  <FormControl>
                    <FormHelperText>
                      <div align="center">Password</div>
                    </FormHelperText>
                    <TextField
                      required={true}
                      type="password"
                      inputProps={{
                        min: 1,
                        style: { textAlign: "center" },
                      }}
                      onChange={this.passwordChanged}
                    />
                  </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                  <Button
                    color="primary"
                    variant="contained"
                    onClick={this.loginPressed}
                  >
                    Login!
                  </Button>
                </Grid>
              </Grid>
            </div>
        );
    }
}

export default Login;