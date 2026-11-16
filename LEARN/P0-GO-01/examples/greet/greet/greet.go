// Package greet builds greetings.
package greet

// Hello returns a greeting for name. The capital H makes it visible to other packages.
func Hello(name string) string {
	return "Hello, " + name + "!"
}
