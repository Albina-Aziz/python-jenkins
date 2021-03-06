# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='admin', password='admin123')
print(server)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
params = {
    'port': '22',
    'username': 'ec2-user',
    'credentialsId': '10db1849-dba0-4803-9ad1-0998d0d15543',
    'host': '3.109.200.197'
}
server.create_node('slave5', numExecutors=2, nodeDescription='my test slave', remoteFS=r'/var/lib/jenkins',
                   labels='onbase_agent', exclusive=True, launcher=jenkins.LAUNCHER_SSH, launcher_params=params)

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
