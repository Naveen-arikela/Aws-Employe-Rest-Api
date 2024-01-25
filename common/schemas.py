from marshmallow import Schema, fields, validate

class ProjectSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)

class QualificationSchema(Schema):
    qualificationName = fields.String(required=True)
    fromDate = fields.String(required=True)
    toDate = fields.String(required=True)
    percentage = fields.Float(validate=validate.Range(min=0, max=100), required=True)

class WorkExperienceSchema(Schema):
    companyName = fields.String(required=True)
    fromDate = fields.String(required=True)
    toDate = fields.String(required=True)
    address = fields.String(required=True)

class AddressDetailsSchema(Schema):
    hno = fields.String(required=True)
    street = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)

class EmployeeSchema(Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    age = fields.Integer(validate=validate.Range(min=0))
    gender = fields.String()
    phoneNo = fields.String()
    addressDetails = fields.Nested(AddressDetailsSchema, required=True)
    workExperience = fields.List(fields.Nested(WorkExperienceSchema), required=True)
    qualifications = fields.List(fields.Nested(QualificationSchema), required=True)
    projects = fields.List(fields.Nested(ProjectSchema), required=True)
    photo = fields.String()


class EmployeeID(Schema):
    empID = fields.Integer(required=True)