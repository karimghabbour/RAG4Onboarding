# HPE iLO 


10
QuickSpecs HPE Integrated Lights-Out (iLO)
Standard Features
Page 2
What is different in iLO6
• SPDM support for increased security with storage and network cards
• Telemetry streaming using Redfish Event subscription.
• Redfish APIs for iLO, System TPM measurement and SPDM capable option cards measurements.
• Added capability in iLO for Two Factor Authentication using OTP (One Time Password) for Microsoft AD users
• PLDM Downstream Firmware Update
• Certificate Management Enhancements
• Automatic certificate Enrollment via SCEP
• Certificate sideloading
• Redfish consistent health roll-ups
• Automatic clearing of Redfish alerts when condition doesnotdoes not exist anymore.
• Telemetry streaming using Redfish Event subscription.
• Redfish APIs for iLO, System TPM measurement and SPDM capable option cards measurements.
• Added capability in iLO for Two Factor Authentication using OTP (One Time Password) for Microsoft AD users
What’s deprecated in iLO 6
• Java IRC
• Internet Explorer
• eRS Direct Connect
• Jitter Smoothing
Refer to the HPE iLO User Guide (iLO 6 iLO 5 iLO 4) and release notes (iLO 6 iLO 5 iLO 4) for a complete list of
fixes/enhancements and also additional information on new features/enhancements/fixes.
Flexible Interfaces for HPE ProLiant
Using any of the HPE iLO for ProLiant interfaces, customers can configure, update and control all HPE iLO for ProLiant Standard
functions regardless of the state of the host server or operating system:
• Browser - HPE iLO for ProLiant is fully accessible by means of Google Chrome™, Microsoft® Edge®, and Mozilla Firefox®
(Linux® and Windows® only).
• Redfish API – HPE iLO for ProLiant conforms to industry-standard specification and schema for data center infrastructure
management sponsored and controlled by the Distributed Management Task Force, Inc. (DMTF), Redfish establishes a new
management standard for system control that is scalable, easy to use, and secure with the effort to modernize heterogeneous
data centers. In addition, HPE ProLiant servers expose iLO RESTful API extensions, allowing customers to experience the full
range of value-add features available from a programmable interface.
• Command line - HPE iLO for ProLiant supports the new industry standard command line, DMTF System Management
Architecture for Server Hardware, Server Management Command Line Protocol (SM CLP) specification. T
• Scripting - HPE iLO for ProLiant supports a scalable scripting interface based on Redfish and JSON (iLOREST and Powershell
Cmndlet) For legacy backward compatibility, XML or PERL scripting (RIBCL) is also available but HPE recommends Redfish
based scripting utilities. This enables scalable, simultaneous configuration, update and operation large groups of HPE iLO for
ProLiant servers
• Intelligent Platform Management Interface (IPMI) is a standardized computer system interface used by system
administrators for out-of-band management of computer systems and monitoring of their operation. System administrators can
use IPMI messaging to monitor platform status (e.g. system temperatures, voltages, fans, power supplies and chassis intrusion);
to query inventory information; to review hardware logs of out-of-range conditions; or to perform recovery procedures such as
issuing requests from a remote console through the same connections e.g. system power-down and rebooting, or configuring
watchdog timers. While iLO offers IPMI for legacy backward compatibility, HPE recommends customers to use Redfish which is
a modern and secure management interface. The standard also defines an alerting mechanism for the system to send a simple
network management protocol (SNMP) platform event trap (PET).
QuickSpecs HPE Integrated Lights-Out (iLO)
Standard Features
Page 3
iLO Features
Provisioning
• Always On Intelligent Provisioning
Intelligent Provisioning is now Always On. Intelligent Provisioning is accessible from the iLO browser user interface anytime
without having to reboot your server. Clicking Always On to access Intelligent Provisioning has the same capabilities as
accessing Intelligent Provisioning by pressing F10 from the POST screen.
• Auto-Configuration of IP Address using DNS/DHCP for HPE ProLiant
HPE Integrated Lights-Out (iLO) for ProLiant provides automatic network configuration. A default name and Dynamic Host
Configuration Protocol (DHCP) client that leases an IP address from the DHCP server on the network are standard with HPE
iLO for ProLiant. This allows the management processor to register its device name with Domain Name Services (DNS). For
systems that do not use DNS/DHCP, static IP configuration is also supported.
• Flexible Network Connectivity for HPE ProLiant
HPE Integrated Lights-Out (iLO) for ProLiant provides a choice between two network connection methods to access all
functionality:
Dedicated connection - Access HPE iLO for ProLiant via an embedded 10/100/1000-MB dedicated Ethernet NIC.
This enables remote management over a dedicated, out-of-band management network. In-band SNMP notification of
server problems on a real-time basis is also supported without separate telephone connections or modem sharing
devices. The dedicated NIC can auto-negotiate speed and duplex options. The iLO Dedicated NIC provides the highest
levels of reliability and security.
Shared Network Port - On selected ProLiant server models, HPE iLO for ProLiant supports network connectivity
through a new high-speed shared connection via one of the embedded system NICs. The latest version of iLO also
supports. Shared network port over the Flexible -LOM providing full accessibility to all HPE iLO for ProLiant functions
including browser, Virtual Media and Virtual Keyboard Video and Mouse in graphics mode. The management processor
maintains a unique IP address and MAC allowing the network controller to route HPE iLO for ProLiant and host data
correctly. With the Shared Network Port, out-of-band management and production data can share the same wire
eliminating the separate network connection for each server.
• Flexible Setup Options for HPE ProLiant
An onboard ROM-based configuration utility allows fast and easy setup without additional software. HPE iLO for ProLiant can
also be setup via the browser or command line interface over the network. Integration with SmartStart Scripting Toolkit allows
configuration of the card as part of the initial server deployment. For large deployments, the HPE Lights-Out Configuration
Utility or the iLO REST tool can be used to configure groups of HPE iLO for ProLiant processors, saving time and resources.
• iLO IDevID
iLO can be provisioned with server identity in the factory. This factory provisioned server identity is called iLO IDevID.
HPE servers can be securely on boarded into a customer network using the IDevID for 802.1X authentication. iLO
IDevID has life time validity and is immutable. To instruct the HPE factory to provision a server with an IDevID, include
SKU P41905-B21 in your order. Storage space earmarked in the iLO which can be used as a repository for firmware,
drivers and software components. The components can be organized in to install sets and can be used to
rollback/patch faulty firmware.
• iLO Service Port (Gen10 servers and above only)
The iLO Service port is a USB port connected to the iLO and is located on the front panel of the server. Users can connect
their laptops to this port via a USB-Ethernet adapter (HPE recommends using the following HPE part Q7Y55A) and get the
full access to the Integrate remote console. Users can also connect a USB drive to this port and download service logs to it.
All servers may not have an iLO Service Port please refer server QuickSpecs to confirm.
• ROM-base Setup Utility (RBSU) for HPE ProLiant
Embedded configuration utility within the system ROM and accessible through the HPE Integrated Lights-Out (iLO) for
ProLiant interface that facilitates pre-OS display of server resources, configuration of primary boot controller and boot order,
and configuration of system devices and installed options.
QuickSpecs HPE Integrated Lights-Out (iLO)
Standard Features
Page 4
• Remote Serial Console (Virtual Serial Port) for HPE ProLiant
Access to the host server's serial, text-based (Virtual Serial Port) during all server states over an Ethernet network is
a standard feature on all HPE Integrated Lights-Out for ProLiant management processors. From the operating
system-independent console you can monitor and control the BIOS and the server during Power-On System start-up
testing (POST), as well as Microsoft Emergency Management Services® and serial tty sessions on systems running
Linux operating systems. After OS is installed access can be set up to be re-directed to the Virtual Serial Port. Also in
the event of a crash you can configure the OS to send the core data dumps to the Virtual Serial port.
Inventory, Health Management and Firmware Update
• HPE Agentless Management 2.0
The base hardware monitoring and alerting capability is built into the system (running on the HPE iLO chipset) and starts
working the moment that a power cord and an Ethernet cable is connected to the server. This means that:
– All core management is out-of-band for increased security and stability: no OS software required, no open SNMP port
on the OS and zero downtime updates
– Monitor and Alerting on key internal server components: CPUs, memory, temperatures, fans, SmartArray controllers,
hard drives (including cache modules) and power supplies
– iLO integrates with HPE GreenLake for Compute Ops Management
– iLO integrates with HPE OneView
Notes: On Gen10 and later generation servers, server monitoring is only via Agentless Management, HPE does not provide
HPE Insight Management Agents or HPE WBEM providers for Gen10 servers.
• Simple Network Management Protocol Version 3 (SNMPv3)
SNMP is the protocol developed to manage nodes (servers, workstations, routers, switches and hubs etc.) on an IP network.
HPE iLO now has SNMP Version 3 (SNMPv3) which has added security and remote configuration capabilities over the previous
versions. The SNMPv3 architecture introduces the User-based Security Model (USM) for message security and the View-based
Access Control Model (VACM) for access control. The architecture supports the concurrent use of different security, access
control, and message processing models. More specifically: Security, authentication and privacy, authorization and access
control, Administrative Framework, naming of entities, people and policies, usernames and key management, notification
destinations, proxy relationships, and remotely configurable via SNMP operations
• HPE Active Health System
HPE Active Health System is an essential component of the HPE iLO Management. It provides customers with: Diagnostics
tools/scanners wrapped into one; Always on, continuous monitoring for increased stability and shorter downtimes; Rich
configuration history; Health and service alerts; Easy export and upload to Service and Support
QuickSpecs HPE Integrated Lights-Out (iLO)
Standard Features
Page 5
• Alert Administration for HPE ProLiant
HPE Integrated Lights-Out (iLO) for ProLiant support delivery of SNMP server agent alerts as well as internally generated
management processor alerts (e.g. unsuccessful login attempt), to a management console such as HPE GreenLake for Compute
Ops Management and HPE OneView. Traps forwarded by the processor can be configured in Insight Manager for delivery to an
administrator's pager or e-mail.
• Automatic and On-Demand Video Record and Playback for HPE ProLiant
HPE ProLiant iLO Console Replay captures and stores for replay the console video during a server's last major fault or boot
sequence. Server faults include an ASR, server boot sequence, Linux panic, or Windows® blue screen. Additionally, users are
able to manually record and save any console video sequence to their client hard drive for replay from the HPE iLO Integrated
Remote Console.
• Embedded System Health for HPE ProLiant
On supported server models, the HPE iLO for ProLiant management processor monitors fans, temperature sensors, power
supply sensors and VRMs without having the System Management Driver loaded. The status of these is accessible from all HPE
iLO for ProLiant user interfaces (browser, SMASH command line Redfish API, XML scripts and IPMI) independent of the host
operating system The intelligence of iLO manages the Sea of Sensors thermal control, directs the Dynamic Power Capping
technology and monitors the health of server components.
• HPE Embedded Remote Support
Hewlett Packard Enterprise offers embedded remote support that allows a customer to enable remote support from iLO,
greatly reducing the time to activate remote monitoring. iLO remote support works seamlessly with Insight Remote Support
and OneView Remote Support to enable customers to benefit from 24x7 remote monitoring, auto-generated service events,
and support cases which can all be managed in the HPE Support Center portal.
• Integrated Lights-Out (iLO) Event Log for HPE ProLiant
The HPE iLO for ProLiant Event Log stores detailed management processor events and data independent of the host
operating system. Actions like server power on/off, reset, changes in user configuration, clear event log, successful and
unsuccessful login attempts are logged along with the user's access machine name in the iLO Event Log enabling audits for
security or troubleshooting purposes. The iLO Event Log is easily accessible through the browser, command line, script or
Insight Manager.
• Integrated Management Log for HPE ProLiant
HPE Integrated Lights-Out (iLO) for ProLiant captures and stores the server's Integrated Management Log (IML) for access
via browser or command line even when the server is not operational. This capability can be helpful when troubleshooting
remote host server problems. The IML contains a history of events that impact server health and management.
• Integration with HPE GreenLake for Compute Ops Management and HPE OneView
HPE Integrated Lights-Out (iLO) for ProLiant is integrated with Hewlett Packard Enterprise and other leading management
applications to allow seamless use in lifecycle tasks and processes from deployment to fault management and administration.
HPE GreenLake for Compute Ops management and HPE OneView intelligently discovers HPE iLO for ProLiant devices and
associates them with their host servers for fast access during fault management activities.
QuickSpecs HPE Integrated Lights-Out (iLO)
Standard Features
Page 6
• Integrated Remote Console for HPE ProLiant
The HPE iLO .NET Integrated Remote Console is launched from the iLO web browser interface, utilizes Microsoft .NET
Framework® 3.5 (on the client PC ) and takes advantage of Microsoft DirectX® based hardware acceleration to provide high
performance and outstanding user graphics. HPE iLO has an enriched viewing experience with maximum resolution of 1600 x
1200 and maximum color depth of 32k colors. With HPE iLO, remote screen fits within one window and the screen can be
scaled to any size, avoiding the use of scroll bars.
HPE iLO for ProLiant has a Java-free Integrated Remote Console for environments with Microsoft Windows® host and client
operating systems. With HPE iLO Standard and HPE iLO Standard Blade Edition, Integrated Remote Console provides access to
Virtual Keyboard Video and Mouse in pre-OS text mode and Virtual power from a single screen. ProLiant OA/iLO Standard
Blade Edition also allows virtual media to be controlled from the IRC.
Starting with iLO 5 v1.20 onwards a HTML5 remote console is supported.
• Local User Accounts And Logon Records for HPE ProLiant
HPE Integrated Lights-Out (iLO) for ProLiant Standard supports local user accounts with customizable access rights, individual
logins and passwords. HPE iLO for ProLiant also provides logging of user actions in the event log, progressive delays for failed
login attempts, and login legal warning.
• Microsoft Emergency Management Service Console Integration for HPE ProLiant
The Microsoft Emergency Management Service® console provides a text-based screen to access the host server. HPE
Integrated Lights-Out (iLO) for ProLiant provides the option to access the EMS console from the Integrated Lights-Out (iLO)
browser interface. The Emergency Management Service console option is available on all HPE ProLiant servers using Windows
Server 2003® or later.
• Multi-Language Support
We provide our customers with the ability to read the HPE iLO GUI in the following languages: English, Japanese and simplified
Chinese. Multi-Language support is only available on servers which carry a version of iLO with NAND.
• Remote Firmware Update for HPE ProLiant
This feature ensures that HPE Integrated Lights-Out (iLO) for ProLiant is always up-to-date with the latest firmware available
from Hewlett Packard Enterprise. Updates to the ROM code on HPE iLO for ProLiant are accomplished through the browser
interface, command line, REST API , XML script, or using online flash components for Windows® Linux® and VMware®.
• System Diagnostics for HPE ProLiant
HPE Integrated Lights-Out (iLO) for ProLiant may be used to diagnose systems. The Remote Console, Integrated Remote
Console and Remote Serial Console may be used to monitor the system for POST error messages. The Integrated Management
Log and HPE iLO for ProLiant Event Log record events useful for diagnostics. HPE Integrated Lights-Out (iLO) for ProLiant
Virtual Media (if activated by an iLO Advanced key) may be used to boot and run System Diagnostics.
• Virtual Indicators for HPE ProLiant
HPE Integrated Lights-Out (iLO) for ProLiant provides the ability to control server Unit ID LEDs from the HPE iLO browser,
REST API command line (SM CLP), XML scripting. The server Unit ID LED is the blue LED on the ProLiant server that is used
for identifying systems in a rack full of servers.
• Virtual Key Video Mouse remote text console for HPE ProLiant
Embedded hardware remote console capabilities in a text mode screen prior to loading of the operating system; is provided as
a standard feature on all ProLiant Integrated Lights-Out (iLO) management processors. This provides access to system BIOS
and during Power-On System start-up testing using Virtual KVM technology. Remote text in "pre-OS" mode is accessible from
the Integrated Remote Console and HTML5 Remote Console.
• Virtual Power Button for HPE ProLiant
Using a supported browser, command line or script interface, HPE Integrated Lights-Out (iLO) for ProLiant can be used to
remotely operate the power button of a host. For example, if the host server is off, you can turn it on from the HPE ProLiant
iLO browser, REST API, command line (SM CLP), XML. You can also power off and on the server in one step. A "press and hold"
option is available for the Virtual Power Button in the event a momentary press is insufficient to power off a server
experiencing an operating system failure.
• Virtual Private Network (VPN) support for HPE ProLiant
HPE iLO for ProLiant functionality is available securely over the Internet around the world when used in conjunction with VPN
technology. VPN is supported on both HPE iLO for ProLiant network connection methods, dedicated and shared network ports.
QuickSpecs HPE Integrated Lights-Out (iLO)
Standard Features
Page 7
• IPv6 on Dedicated NIC
The HPE iLO dedicated NIC supports IPv6 addressing. DHCPv6, SLAAC/router assigned addresses and static IPv6 addresses
are supported.
• Video Player for HPE ProLiant
HPE iLO allows you to view automatically captured server video footage or on-demand captured footage within an iLO session
or separately through the new iLO Video Player.
• Virtual Keyboard Video and Mouse graphic console for HPE ProLiant
HPE iLO graphical consoles provide Virtual KVM capabilities with KVM over IP performance. This gives system administrators a
single console that is responsive and agile for routine administration and emergency situations. iLO Virtual KVM works with a
standard browser and no additional software is required on the remote server or client system for iLO 2. HPE iLO 3 and iLO 4
require the .NET Framework 3.5, which is already provided with Windows® 7.
• Virtual Media for HPE ProLiant
The USB-based Virtual Media feature allows an IT administrator to boot the remote server using a standard 1.44-MB diskette,
CD ROM, DVD+R or USB flash drive on a client PC or from a floppy diskette, CD or DVD image stored on a virtual media server
on the network. Virtual Media saves time and increases efficiency by eliminating the need to visit servers in datacenters and
remote sites just to insert a diskette, CD-ROM, DVD-ROM or USB key.
• iLO Serial Port Record\ Playback for HPE ProLiant
HPE iLO takes the output data from the Remote Virtual Serial Console (VSP) and saves it to iLO memory for so data can be
later accessed. Very similar to "video console replay ", but is text based data only from the serial port. This would be used to
store logs of data and\or history of activity to be retrieved later to see exactly what activity was done - or actions occurred
(Play back) but all text based.
• Intelligent System Tuning (Core Boosting) (iLO 5 and above only)
When enabling Intel Turbo Boost mode, Core Boosting will maintain higher frequencies across more active cores on select
servers and Intel processors; This is accomplished while maintaining Intel specs, warranty, and reliability. To enable this
capability iLO Advanced license is needed.
• Remote Kernel Debugger for Windows® for HPE ProLiant
On a remote PC to the iLO Virtual Serial Port (VSP) to diagnose and repair operating system kernel errors.
• Remote System logs
HPE iLO keeps a log of everything being done, so it can later be used for troubleshooting or simply has a record. Syslog can be
configured to receive logging from a remote client, or to send logging to a remote syslog server. Remote logging is sending a
duplicate record of those events not only to the local machine but to a remote machine as well.
Workload Performance Advisor Provides server tuning recommendations to improve server performance on Intel Xeon
based server models.
• iLO Restful Application Program Interface (API)
The iLO RESTful API management interface functionality is available for iLO 4, iLO 5, iLO 6 and Moonshot iLO Chassis
Management Module-based. Hewlett Packard Enterprise servers uses the basic HTTP operations (GET, PUT, POST, DELETE,
and PATCH) to either submit or return a JSON formatted “resource” to or from a URI. The API enables users to manage one or
multiple servers to:
Get full inventory
Control Power and reset
Configure BIOS, iLO 4, iLO 5, iLO 6 and Smart Array (supported only on iLO 5/Gen10 controllers and above) settings
Status of server health
Fetch event logs and SSH Serial Console
And more
iLO RESTful API Redfish conformant. To learn more, see the iLOrest user guide overview (hpe.com)
QuickSpecs HPE Integrated Lights-Out (iLO)
Standard Features
Page 8
Security
HPE Integrated Lights-Out (iLO) for ProLiant provides strong security for remote management in distributed IT environments by
using industry-standard Secure Sockets Layer (SSL) and Transport Layer Security (TLS) encryption of HTTP data transmitted
across the network. SSL or TLS encryption (up to 256-bit) ensures that the HTTP information is secure as it travels across the
network.
HPE Integrated Lights-Out (iLO) for ProLiant also uses Secure Shell version 2 to provide strong authentication and encryption of
commands executed on iLO management processors over a network. PuTTY and OpenSSH clients may be used to access HPE iLO
for ProLiant over a Secure Shell connection.
In addition, HPE iLO for ProLiant provides a configurable option to enable strong encryption Advanced Encryption Standard (AES)
on browser, REST API, CLP and XML scripting interfaces.
• ILO Silicon Root of Trust (iLO 5 and later only)
Signatures for validation of integrity of iLO and UEFI/BIOS are built into the iLO ASIC. This prevents any possibility of
tampering of security signatures throughout the supply-chain.
• Security Protocol and Data Model
iLO uses the Security Protocol and Data Model (SPDM) to verify the integrity of components and authenticate the Option
Cards. All the components do not support SPDM. If SPDM is enabled, an unsupported or non-authentic component will change
the iLO security status to Risk A
• Automatic certificate enrollment
iLO now supports obtaining and renewing SSL certificate automatically using the Simple Certificate Enrollment Protocol
(SCEP). Currently, iLO supports these features on the Microsoft Network Device Enrollment Service (NDES).
• 3 rd Party Key Manager Support
Facilitates key exchange for disk connect to a smart array controller, encrypted by Utimaco and Thales key managers –
providing easy integration of ProLiant servers in environments where the encryption key management is done by Utimaco
ESKM, Thales TCT KeySecure for Government G350v, Thales KeySecure k150v or Thales CipherTrust Manager 2.2.0 virtual
(k170v) and physical (k570) appliances:
Automatic Firmware Recovery (iLO 5 and above only)
Recover iLO, UEFI/BIOS and other essential firmware automatically to a known good version (either factory default
or a known good firmware recipe resident in the iLO Repository) on detection of a compromised iLO, UEFI/BIOS
and other essential firmware.
• Commercial National Security Algorithms mode (CNSA) support (iLO 5 and above only) Directory Services Integration
for HPE ProLiant
Support for CNSA compliant cryptography preventing the use of insecure algorithms.
Directory Services Integration for HPE ProLiant HPE Integrated Lights-Out (iLO) for ProLiant integrates with enterprise-
class directory services to provide secure, scalable, and cost effective user management. Directory services, such as Microsoft®
Active Directory Novell eDirectory and OpenLDAP (iLO 4 v2.53), can be used to authorize directory users with assigned user
roles to Integrated Lights-Out processors. With Active Directory, customers have the flexibility to integrate with or without a
schema extension. An easy and reliable installation program is available to install a management console snap-in and extend
customer's existing directory schema to enable directory support for the HPE lights-out management products. A directory
migration tool is available to automate setup for both methods of integration. In addition, current versions of HPE iLO firmware
will support directory nested groups.
QuickSpecs HPE Integrated Lights-Out (iLO)
Standard Features
Page 9
• One-Button Secure Erase
Easily erase all user data on the server, secondary storage and NVRAM, per NIST Standards 800-88r1 with the click of a
button in the UI/one call via RESTful API. Allowing easy repurpose and redeployment of servers with confidence that servers
have been reset back to factory settings.
• Runtime Firmware Validation (iLO 5 and above only) Server Configuration Lock
Validation of iLO and UEFI/BIOS firmware at runtime. Notification and automated recovery on detection of compromised
firmware.
Ensures secure transit and locks server hardware configuration using a password.
• Single Sign-On for HPE ProLiant
ProLiant users can automatically login to iLO from HPE OneView. In addition, to direct access and authentication using iLO
Active Directory integration, the role based authentication in HPE OneView can be used to simplify user access and user
account administration.
• Two-factor authentication via Kerberos for HPE ProLiant
HPE ProLiant Integrated Lights-Out (iLO) provides strong user authentication with two-factor authentication via Kerberos or
smart cards such as Common Access Card (CAC) and Personal Identity Verification (PIV) cards using digital certificates
embedded on smartcards or USB -security tokens. Using this form of strong authentication, iLO access can be restricted only to
IT individuals possessing a certificate bearing smartcard or USB security token and a PIN.
QuickSpecs HPE Integrated Lights-Out (iLO)
Service and Support
Page 10
HPE Services
No matter where you are in your digital transformation journey, you can count on HPE Services to deliver the expertise you need
when, where and how you need it. From planning to deployment, ongoing operations and beyond, our experts can help you realize
your digital ambitions.
https://www.hpe.com/services
HPE Services
iLO Care Pack options can be found at
https://ssc.hpe.com/portal/site/ssc?action=determineNodeContents&nodeId=28814
Consulting Services
No matter where you are in your journey to hybrid cloud, experts can help you map out your next steps. From determining what
workloads should live where, to handling governance and compliance, to managing costs, our experts can help you optimize your
operations.
https://www.hpe.com/services/consulting
HPE Managed Services
HPE runs your IT operations, providing services that monitor, operate, and optimize your infrastructure and applications, delivered
consistently and globally to give you unified control and let you focus on innovation.
HPE Managed Services | HPE
Operational services
Optimize your entire IT environment and drive innovation. Manage day-to-day IT operational tasks while freeing up valuable time
and resources. Meet service-level targets and business objectives with features designed to drive better business outcomes.
https://www.hpe.com/services/operational
HPE Complete Care Service
HPE Complete Care Service is a modular, edge-to-cloud IT environment service designed to help optimize your entire IT
environment and achieve agreed upon IT outcomes and business goals through a personalized experience. All delivered by an
assigned team of HPE Services experts. HPE Complete Care Service provides:
A complete coverage approach -- edge to cloud
An assigned HPE team
Modular and fully personalized engagement
Enhanced Incident Management experience with priority access
Digitally enabled and AI driven customer experience
https://www.hpe.com/services/completecare
HPE Lifecycle Services
HPE Lifecycle Services provide a variety of options to help maintain your HPE systems and solutions at all stages of the product
lifecycle. A few popular examples include:
Lifecycle Install and Startup Services: Various levels for physical installation and power on, remote access setup, installation and
startup, and enhanced installation services with the operating system.
HPE Firmware Update Analysis Service: Recommendations for firmware revision levels for selected HPE products, taking into
account the relevant revision dependencies within your IT environment.
HPE Firmware Update Implementation Service: Implementation of firmware updates for selected HPE server, storage, and solution
products, taking into account the relevant revision dependencies within your IT environment.
QuickSpecs HPE Integrated Lights-Out (iLO)
Standard Features
Page 11
Implementation assistance services: Highly trained technical service specialists to assist you with a variety of activities, ranging
from design, implementation, and platform deployment to consolidation, migration, project management, and onsite technical
forums.
HPE Service Credits: Access to prepaid services for flexibility to choose from a variety of specialized service activities, including
assessments, performance maintenance reviews, firmware management, professional services, and operational best practices.
Notes: To review the list of Lifecycle Services available for your product go to:
https://www.hpe.com/services/lifecycle
For a list of the most frequently purchased services using service credits, see the HPE Service Credits Menu
Defective Media Retention
An option available with HPE Complete Care Service and HPE Tech Care Service and applies only to Disk or eligible SSD/Flash
Drives replaced by HPE due to malfunction.
Consult your HPE Sales Representative or Authorized Channel Partner of choice for any additional questions and services options.
Parts and Materials
HPE will provide HPE-supported replacement parts and materials necessary to maintain the covered hardware product in
operating condition, including parts and materials for available and recommended engineering improvements.
Parts and components that have reached their maximum supported lifetime and/or the maximum usage limitations as set forth in
the manufacturer's operating manual, product quick-specs, or the technical product data sheet will not be provided, repaired, or
replaced as part of these services.
How to Purchase Services
Services are sold by Hewlett Packard Enterprise and Hewlett Packard Enterprise Authorized Service Partners:
Services for customers purchasing from HPE or an enterprise reseller are quoted using HPE order configuration tools.
Customers purchasing from a commercial reseller can find services at https://ssc.hpe.com/portal/site/ssc/
AI Powered and Digitally Enabled Support Experience
Achieve faster time to resolution with access to product-specific resources and expertise through a digital and data driven
customer experience
Sign into the HPE Support Center experience, featuring streamlined self-serve case creation and management capabilities with
inline knowledge recommendations. You will also find personalized task alerts and powerful troubleshooting support through an
intelligent virtual agent with seamless transition when needed to a live support agent.
https://support.hpe.com/hpesc/public/home/signin
Consume IT On Your Terms
HPE GreenLake edge-to-cloud platform brings the cloud experience directly to your apps and data wherever they are—the edge,
colocations, or your data center. It delivers cloud services for on-premises IT infrastructure specifically tailored to your most
demanding workloads. With a pay-per-use, scalable, point-and-click self-service experience that is managed for you, HPE
GreenLake edge-to-cloud platform accelerates digital transformation in a distributed, edge-to-cloud world.
Get faster time to market
Save on TCO, align costs to business
Scale quickly, meet unpredictable demand
Simplify IT operations across your data centers and clouds
---- 

