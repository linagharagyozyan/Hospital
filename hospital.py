class Node(object):
    def __init__(self):
        self.next = None

class Job(Node):
    def __init__(self, name):
        super(Job, self).__init__()
        self.name = name

class Doctor(Node):
    def __init__(self, name, surname, speciality, phone):
        super(Doctor, self).__init__()
        self.name = name
        self.surname= surname
        self.email = "{}{}{}{}".format(self.name.lower(),"_",self.surname.lower(),"@gmail.com")
        self.speciality = speciality
        self.phone = phone

class Patient(Node):
    def __init__(self, name, surname, disease, status, phone):
        super(Patient, self).__init__()
        self.name = name
        self.surname = surname
        self.email = "{}{}{}{}".format(self.name.lower(),"_",self.surname.lower(),"@gmail.com")
        self.disease = disease
        self.status = status
        self.phone = phone

class Hospital:
    def __init__(self, name, address, phone):
        self.__Jobhead = None
        self.__Doctorhead = None
        self.__Patienthead = None
        self.name = name
        self.address = address
        self.phone = phone
        self.email = "{}{}{}{}".format("hospital","_",self.name.lower(),"@gmail.com")

    def addJob(self, new_job):
        job = Job(new_job)
        if self.__Jobhead == None:
            self.__Jobhead = job
        else:
            temp = self.__Jobhead
            while temp.next is not None:
                temp = temp.next

            newJob = job
            temp.next = newJob

    def addDoctor(self, name, surname, specialty, phone):
        doctor = Doctor(name, surname, specialty, phone)
        if self.__Doctorhead == None:
            self.__Doctorhead = doctor
        else:
            temp = self.__Doctorhead
            while temp.next is not None:
                temp = temp.next

            newDoctor = doctor
            temp.next = newDoctor

    def addPatient(self, name, surname, disease, status, phone):
        patient = Patient(name, surname, disease, status, phone)
        if self.__Patienthead == None:
            self.__Patienthead = patient
        else:
            temp = self.__Patienthead
            while temp.next is not None:
                temp = temp.next

            newPatient = patient
            temp.next = newPatient

    def deleteJob(self, job):
        if self.__Jobhead == None:
            print "There are no jobs in the list!"
        elif self.__Jobhead.name == job:
            self.__Jobhead = self.__Jobhead.next
        else:
            temp = self.__Jobhead
            while temp.next is not None and temp.next.name != job:
                temp = temp.next
            if temp.name == job:
                temp.next = temp.next.next
            else:
                print "There is no such job in our list!"

    def deleteDoctor(self, name, surname):
        if self.__Doctorhead == None:
            print "There are no doctors in the list!"
        elif self.__Doctorhead.name == name and self.__Doctorhead.surname == surname:
            self.__Doctorhead = self.__Doctorhead.next
        else:
            temp = self.__Doctorhead
            while temp.next is not None and temp.next.name != name and temp.next.surname != surname:
                temp = temp.next
            if temp.name == name and temp.surname == surname:
                temp.next = temp.next.next
            else:
                print "There is no such doctor in our list!"

    def deletePatient(self, name, surname):
        if self.__Patienthead == None:
            print "There are no patients in the list!"
        elif self.__Patienthead.name == name and self.__Patienthead.surname == surname:
            self.__Patienthead = self.__Patienthead.next
        else:
            temp = self.__Patienthead
            while temp.next is not None and temp.next.name != name and temp.next.surname != surname:
                temp = temp.next
            if temp.name == name and temp.surname == surname:
                temp.next = temp.next.next
            else:
                print "There is no such patient in our list!"

    def getHospitalInfo(self):
        print "Welcome to Hospital", self.name, "\n""Contact details:""\n""---------","\n""Address:",self.address,"\n""Email: ",\
              self.email,"\n""Phone: ",self.phone

    def getDoctorInfo(self, name, surname):
        temp = self.__Doctorhead
        while temp.next is not None and temp.name != name and temp.surname != surname:
            temp = temp.next
        if temp.name == name and temp.surname == surname:
            print "\n""Name: ", temp.name, "\n""Surname: ", temp.surname, "\n""Email: ", temp.email, \
                  "\n""Speciality: ", temp.speciality, "\n""Phone: ", temp.phone, "\n", "---------"
        else:
            print "There is no such doctor in our list!"

    def getPatientInfo(self, name, surname):
        temp = self.__Patienthead
        while temp.next is not None and temp.name != name and temp.surname != surname:
            temp = temp.next
        if temp.name == name and temp.surname == surname:
            print "\n""Patient info", "\n", "---------", "\n", "Name: ", temp.name, "\n", "Surname: ", temp.surname, "\n", "Email: ", \
                  temp.email, "\n", "Disease: ", temp.disease, "\n", "Status: ", temp.status, "\n", "Phone: ", temp.phone, "\n", "---------"
        else:
            print "There is no such patient in our list!"

def main():
    hospital = Hospital("Nairi", "Paronyan St., 21 Building", "+374-10-537500")
    hospital.getHospitalInfo()

    hospital.addJob("Cardiologist")
    hospital.addJob("Therapist")
    hospital.addJob("Surgeon")

    hospital.addDoctor("Armen","Kirakosyan","Cardiologist","+37477887788")
    hospital.addDoctor("Karen","Petrosyan","Cardiologist","+37491070097")
    hospital.addDoctor("Petros", "Karapetyan","Surgeon","+37498288888")

    hospital.addPatient("Tigran","Khachatryan","High blood pressure","In progress","+37477887799")
    hospital.addPatient("Gor","Nersisyan","Diabetes","In progress","+37495000000")
    hospital.addPatient("Poghos", "Kaputikyan", "Broken toe", "In progress", "+374394822")

    hospital.getDoctorInfo("Armen", "Kirakosyan")
    hospital.getPatientInfo("Tigran","Khachatryan")
    hospital.getPatientInfo("Gor","Nersisyan")
    hospital.getDoctorInfo("Karen","Petrosyan")



if __name__ == "__main__":
    main()



