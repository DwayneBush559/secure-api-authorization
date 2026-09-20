# Secure API Authorization

A compact Python project demonstrating **object-level authorization** and access-control testing.

The central security rule is simple: knowing or guessing a resource ID is not enough to access that resource. A user must either own the resource or have an authorized administrator role.

## Why this matters

APIs sometimes verify that a user is authenticated without checking whether that user is authorized to access a specific object. That can lead to broken object-level authorization, including IDOR/BOLA-style vulnerabilities.

This project keeps authentication and authorization concerns separate and makes the authorization decision explicit and testable.

## Skills demonstrated

- Python
- Secure API design
- Object-level authorization
- Role-based access control
- IDOR/BOLA prevention
- Negative security testing
- Unit testing

## Test it

```bash
python -m unittest test_authz.py
```

## Tests cover

- the resource owner can read
- another authenticated user is denied
- an authorized administrator can update

## Author

**Dwayne Dwight Bush**  
Software Development • Cybersecurity • AI Systems
