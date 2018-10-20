class HospitalProperties:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Hospital:
    def __init__(self, name, address, phone):
        self.__Jobhead = None
        self.__Doctorhead = None
        self.__Patienthead = None
        self.name = name
        self.address = address
        self.phone = phone
        self.email = "{}{}{}{}".format("hospital","_",self.name.lower(),"@gmail.com")

    def setJobHead(self, new_data):
        self.__Jobhead = HospitalProperties(new_data)

    def setDoctorHead(self, new_data):
        self.__Doctorhead = HospitalProperties(new_data)

    def setPatientHead(self, new_data):
        self.__Patienthead = HospitalProperties(new_data)

    def appendJob(self, new_data):
        temp = self.__Jobhead
        while temp.next is not None:
            temp = temp.next

        newJob = HospitalProperties(new_data)
        temp.next = newJob

    def appendDoctor(self, new_data):
        temp = self.__Doctorhead
        while temp.next is not None:
            temp = temp.next

        newDoctor = HospitalProperties(new_data)
        temp.next = newDoctor

    def appendPatient(self, new_data):
        temp = self.__Patienthead
        while temp.next is not None:
            temp = temp.next

        newPatient = HospitalProperties(new_data)
        temp.next = newPatient

    def getHospitalInfo(self):
        print "Welcome to Hospital", self.name, "\n""Contact details:""\n""---------","\n""Address:",self.address,"\n""Email: ",\
              self.email,"\n""Phone: ",self.phone

    def getJobsInfo(self, data):
        temp = self.__Jobhead
        while temp.next is not None and temp != data:
            temp = temp.next
        print "\n",data.name

    def getDoctorInfo(self, data):
        temp = self.__Doctorhead
        while temp.next is not None and temp != data:
            temp = temp.next
        print "\n""Name: ", data.name, "\n""Surname: ", data.surname, "\n""Email: ", data.email, \
              "\n""Speciality: ", data.speciality, "\n""Phone: ", data.phone

    def getPatientInfo(self, data):
        temp = self.__Patienthead
        while temp.next is not None and temp != data:
            temp = temp.next
        print "\n""Patient info", "\n", "---------", "\n", "Name: ", data.name, "\n", "Surname: ", data.surname, "\n", "Email: ", \
              data.email, "\n", "Disease: ", data.disease, "\n", "Status: ", data.status, "\n", "Phone: ", data.phone, "\n", "---------"

class Job:
    def __init__(self, name):
        self.name = name

class Doctor:
    def __init__(self,name,surname,speciality,phone):
        self.name = name
        self.surname= surname
        self.email = "{}{}{}{}".format(self.name.lower(),"_",self.surname.lower(),"@gmail.com")
        self.speciality = speciality
        self.phone = phone

class Patient:
    def __init__(self,name,surname,disease,status,phone):
        self.name = name
        self.surname = surname
        self.email = "{}{}{}{}".format(self.name.lower(),"_",self.surname.lower(),"@gmail.com")
        self.disease = disease
        self.status = status
        self.phone = phone

def main():
    hospital = Hospital("Nairi", "Paronyan St., 21 Building", "+374-10-537500")

    job1 = Job("Cardiologist")
    hospital.setJobHead(job1)
    job2 = Job("Therapist")
    # append job2

    doctor1 = Doctor("Armen","Kirakosyan","Cardiologist","+37477887788")
    hospital.setDoctorHead(doctor1)
    doctor2 = Doctor("Karen","Petrosyan","Cardiologist","+37491070097")
    # append doctor2

    patient1 = Patient("Tigran","Khachatryan","High blood pressure","In progress","+37477887799")
    hospital.setPatientHead(patient1)
    patient2 = Patient("Gor","Nersisyan","Diabetes","In progress","+37495000000")
    # append patient2

    hospital.getHospitalInfo()

    hospital.getDoctorInfo(doctor1)
    hospital.getPatientInfo(patient1)
    hospital.getPatientInfo(patient2)
    hospital.getDoctorInfo(doctor2)



if __name__ == "__main__":
    main()



