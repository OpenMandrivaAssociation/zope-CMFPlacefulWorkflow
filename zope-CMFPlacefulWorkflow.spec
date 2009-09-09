%define Product CMFPlacefulWorkflow
%define product cmfplacefulworkflow
%define name    zope-%{Product}
%define version 1.2.1
%define bad_version %(echo %{version} | sed -e 's/\\./-/g')
%define release %mkrel 6

%define zope_minver     2.7
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:	    %{name}
Version:    %{version}
Release:    %{release}
Summary:    A Plone product for locally changing the workflow of content types
License:    GPL
Group:      System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{product}-%{bad_version}.tgz
Requires:   zope >= %{zope_minver}
Requires:   zope-Plone >= 2.0.5
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description 
CMF Placeful Workflow is a Plone product allowing to define workflow
policies of content types that can be applied in any sub-folder of
your Plone site.


%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
