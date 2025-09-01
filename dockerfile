FROM apache/hadoop:3

USER root

# Fix CentOS repos to use vault
RUN sed -i 's/mirrorlist=/#mirrorlist=/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org/centos/$releasever|baseurl=http://vault.centos.org/centos/7.9.2009|g' /etc/yum.repos.d/CentOS-*

# Update and install Python 3
RUN yum clean all && \
    yum makecache && \
    yum install -y python3 && \
    yum clean all

USER hadoop
