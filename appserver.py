"""
appserver.py
- creates an application instance and runs the dev server
"""

if __name__ == '__main__':
    from application import create_app

    app = create_app()
    @app.route('/')
    def index():
        return '''
            <ul>
                <li><a href="/user">User</a></li>
                <li><a href="/stripe">Stripe</a></li>
                <li><a href="/fetchdata">Fetchdata</a></li>
            </ul>
        '''
    app.run()
