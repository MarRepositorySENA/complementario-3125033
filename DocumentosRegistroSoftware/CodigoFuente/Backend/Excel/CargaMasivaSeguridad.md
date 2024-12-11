```
//DTO USUARIOEXCELDTO
package com.persona.Backend.Dto;

import java.time.LocalDate;

import com.alibaba.excel.annotation.ExcelProperty;
import com.persona.Backend.Entity.Security.Persona;

public class UsuarioExcelDTO {

	    @ExcelProperty("contrasenia")
	    private String contrasenia;

	    @ExcelProperty("personaId")
	    private Persona personaId;

	    @ExcelProperty("primerNombre")
	    private String primerNombre;

	    @ExcelProperty("segundoNombre")
	    private String segundoNombre;

	    @ExcelProperty("primerApellido")
	    private String primerApellido;

	    @ExcelProperty("segundoApellido")
	    private String segundoApellido;

	    @ExcelProperty("tipoDocumento")
	    private String tipoDocumento;

	    @ExcelProperty("numeroDocumento")
	    private String numeroDocumento;

	    @ExcelProperty("email")
	    private String email;

	    @ExcelProperty("genero")
	    private String genero;

	    @ExcelProperty("direccion")
	    private String direccion;

	    @ExcelProperty("telefono")
	    private String telefono;

	    @ExcelProperty("fechaNacimiento")
	    private LocalDate fechaNacimiento;

	    @ExcelProperty("usuarioName")
	    private String usuarioName;
	    
	    @ExcelProperty("rol")
	    private String rol;
	    
	    @ExcelProperty("modulo")
	    private String modulo;

	    @ExcelProperty("moduloIcono")
	    private String moduloIcono;

	    @ExcelProperty("submodulo")
	    private String submodulo;

	    @ExcelProperty("vista")
	    private String vista;

	    @ExcelProperty("vistaRuta")
	    private String vistaRuta;
	    
		public String getModulo() {
			return modulo;
		}

		public void setModulo(String modulo) {
			this.modulo = modulo;
		}

		public String getModuloIcono() {
			return moduloIcono;
		}

		public void setModuloIcono(String moduloIcono) {
			this.moduloIcono = moduloIcono;
		}

		public String getSubmodulo() {
			return submodulo;
		}

		public void setSubmodulo(String submodulo) {
			this.submodulo = submodulo;
		}

		public String getVista() {
			return vista;
		}

		public void setVista(String vista) {
			this.vista = vista;
		}

		public String getVistaRuta() {
			return vistaRuta;
		}

		public void setVistaRuta(String vistaRuta) {
			this.vistaRuta = vistaRuta;
		}

		public String getRol() {
			return rol;
		}

		public void setRol(String rol) {
			this.rol = rol;
		}

		public String getContrasenia() {
			return contrasenia;
		}

		public void setContrasenia(String contrasenia) {
			this.contrasenia = contrasenia;
		}


		public Persona getPersonaId() {
			return personaId;
		}

		public void setPersonaId(Persona personaId) {
			this.personaId = personaId;
		}

		public String getPrimerNombre() {
			return primerNombre;
		}

		public void setPrimerNombre(String primerNombre) {
			this.primerNombre = primerNombre;
		}

		public String getSegundoNombre() {
			return segundoNombre;
		}

		public void setSegundoNombre(String segundoNombre) {
			this.segundoNombre = segundoNombre;
		}

		public String getPrimerApellido() {
			return primerApellido;
		}

		public void setPrimerApellido(String primerApellido) {
			this.primerApellido = primerApellido;
		}

		public String getSegundoApellido() {
			return segundoApellido;
		}

		public void setSegundoApellido(String segundoApellido) {
			this.segundoApellido = segundoApellido;
		}

		

		public String getTipoDocumento() {
			return tipoDocumento;
		}

		public void setTipoDocumento(String tipoDocumento) {
			this.tipoDocumento = tipoDocumento;
		}

		public String getNumeroDocumento() {
			return numeroDocumento;
		}

		public void setNumeroDocumento(String numeroDocumento) {
			this.numeroDocumento = numeroDocumento;
		}

		public String getEmail() {
			return email;
		}

		public void setEmail(String email) {
			this.email = email;
		}

		public String getGenero() {
			return genero;
		}

		public void setGenero(String genero) {
			this.genero = genero;
		}

		public String getDireccion() {
			return direccion;
		}

		public void setDireccion(String direccion) {
			this.direccion = direccion;
		}

		public String getTelefono() {
			return telefono;
		}

		public void setTelefono(String telefono) {
			this.telefono = telefono;
		}

		public LocalDate getFechaNacimiento() {
			return fechaNacimiento;
		}

		public void setFechaNacimiento(LocalDate fechaNacimiento) {
			this.fechaNacimiento = fechaNacimiento;
		}

		public String getUsuarioName() {
			return usuarioName;
		}

		public void setUsuarioName(String usuarioName) {
			this.usuarioName = usuarioName;
		}

	
	    
	    
	    
}
//SERVICE CARGAMASIVASERVICE
package com.persona.Backend.Service;

import java.time.LocalDateTime;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import com.alibaba.excel.EasyExcel;
import com.persona.Backend.Dto.UsuarioExcelDTO;
import com.persona.Backend.Entity.Security.Modulo;
import com.persona.Backend.Entity.Security.Persona;
import com.persona.Backend.Entity.Security.Role;
import com.persona.Backend.Entity.Security.Usuario;
import com.persona.Backend.Entity.Security.UsuariosRoles;
import com.persona.Backend.Entity.Security.Vista;
import com.persona.Backend.Entity.Security.VistasRoles;
import com.persona.Backend.IService.ICargaMasivaService;
import com.persona.Backend.IService.Security.IModuloService;
import com.persona.Backend.IService.Security.IPersonaService;
import com.persona.Backend.IService.Security.IRoleService;
import com.persona.Backend.IService.Security.IUsuarioService;
import com.persona.Backend.IService.Security.IUsuariosRolesService;
import com.persona.Backend.IService.Security.IVistaService;
import com.persona.Backend.IService.Security.IVistasRolesService;

import io.jsonwebtoken.io.IOException;
import jakarta.transaction.Transactional;

@Service
public class CargaMasivaService implements ICargaMasivaService {
	 @Autowired
	    private IPersonaService personaService;

	    @Autowired
	    private IUsuarioService usuarioService;
	    
	    @Autowired
	    private IRoleService roleService;

	    @Autowired
	    private IUsuariosRolesService usuariosRolesService;
	    
	    @Autowired
	    private IModuloService  moduloService;

	    @Autowired
	    private IVistaService vistaService;

	    @Autowired
	    private IVistasRolesService vistasRolesService;
	    
	    @Autowired
	    private AuditoriaService auditoriaService;

	    @Override
	    public void procesarExcel(MultipartFile file) throws Exception {
	        try {
	            List<UsuarioExcelDTO> usuariosExcelList = EasyExcel.read(file.getInputStream())
	                    .head(UsuarioExcelDTO.class)
	                    .sheet()
	                    .doReadSync();

	            for (UsuarioExcelDTO excelDTO : usuariosExcelList) {
	                try {
	                    guardarUsuarioDesdeExcel(excelDTO);
	                } catch (Exception e) {
	                    System.err.println("Error al procesar el usuario: " + excelDTO.getUsuarioName());
	                    e.printStackTrace();
	                }
	            }
	        } catch (IOException e) {
	            throw new RuntimeException("Error al procesar el archivo Excel: " + e.getMessage());
	        }
	    }

	    @Transactional
	    private void guardarUsuarioDesdeExcel(UsuarioExcelDTO excelDTO) throws Exception {
	        try {
	            // Crear y guardar la entidad Persona
	            Persona persona = new Persona();
	            persona.setPrimerNombre(excelDTO.getPrimerNombre());
	            persona.setSegundoNombre(excelDTO.getSegundoNombre());
	            persona.setPrimerApellido(excelDTO.getPrimerApellido());
	            persona.setSegundoApellido(excelDTO.getSegundoApellido());
	            persona.setTipoDocumento(excelDTO.getTipoDocumento());
	            persona.setNumeroDocumento(excelDTO.getNumeroDocumento());
	            persona.setEmail(excelDTO.getEmail());
	            persona.setGenero(excelDTO.getGenero());
	            persona.setDireccion(excelDTO.getDireccion());
	            persona.setTelefono(excelDTO.getTelefono());
	            persona.setFechaNacimiento(excelDTO.getFechaNacimiento());
	            auditoriaService.setAuditOnCreate(persona);
	            Persona personaGuardada = personaService.save(persona);

	            // Crear y guardar el Usuario
	            Usuario usuario = new Usuario();
	            usuario.setContrasenia(excelDTO.getContrasenia()); // Encriptar la contraseña
	            usuario.setPersonaId(personaGuardada);
	            usuario.setUsuarioName(excelDTO.getUsuarioName());
	            auditoriaService.setAuditOnCreate(usuario);
	            Usuario usuarioGuardado = usuarioService.saveUsuarioJwt(usuario);

	            // Validar y registrar el rol
	            Role role = roleService.findByNombre(excelDTO.getRol());
	            if (role == null) {
	                role = new Role();
	                role.setNombre(excelDTO.getRol());
	                role.setDescripcion("Descripción del rol: " + excelDTO.getRol());
	                auditoriaService.setAuditOnCreate(role);
	                role = roleService.save(role);
	            }

	            // Registrar la relación en UsuariosRoles
	            UsuariosRoles usuariosRoles = new UsuariosRoles();
	            usuariosRoles.setUsuarioId(usuarioGuardado);
	            usuariosRoles.setRoleId(role);
	            auditoriaService.setAuditOnCreate(usuariosRoles);
	            usuariosRolesService.save(usuariosRoles);
	            
	            // Crear y guardar el módulo y sus submódulos
	            Modulo modulo = moduloService.findByNombre(excelDTO.getModulo());
	            if (modulo == null) {
	                modulo = new Modulo();
	                modulo.setNombre(excelDTO.getModulo());
	                modulo.setRuta("/" + excelDTO.getModulo().toLowerCase());
	                modulo.setIcono("icono_" + excelDTO.getModulo().toLowerCase());
	                auditoriaService.setAuditOnCreate(modulo);
	                modulo = moduloService.save(modulo);
	            }

	            // Crear y guardar la vista asociada al módulo
	            Vista vista = vistaService.findByNombre(excelDTO.getVista());
	            if (vista == null) {
	                vista = new Vista();
	                vista.setNombre(excelDTO.getVista());
	                vista.setRuta("/" + excelDTO.getVista().toLowerCase());
	                vista.setModuloId(modulo);
	                auditoriaService.setAuditOnCreate(vista);
	                vista = vistaService.save(vista);
	            }

	            // Registrar la relación entre vistas y roles en VistasRoles
	            VistasRoles vistasRoles = new VistasRoles();
	            vistasRoles.setRoleId(role);
	            vistasRoles.setVistaId(vista);
	            auditoriaService.setAuditOnCreate(vistasRoles);
	            vistasRolesService.save(vistasRoles);

	        } catch (Exception e) {
	            System.err.println("Error al guardar el usuario con los datos del Excel: " + excelDTO.getUsuarioName());
	            e.printStackTrace();
	            throw e;
	        }
	   
}
}
//CONTROLLER CARGAMASIVACONTROLLER
package com.persona.Backend.Controller.Security;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import com.persona.Backend.IService.ICargaMasivaService;
@CrossOrigin(origins = "http://localhost:4200")
@RestController
@RequestMapping("/api/carga-masiva")
public class CargaMasivaController {
    @Autowired
    private ICargaMasivaService cargaMasivaService;
    @PostMapping(value = "/usuarios", consumes = MediaType.MULTIPART_FORM_DATA_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> cargarUsuarios(@RequestParam("file") MultipartFile file) {
        try {
            cargaMasivaService.procesarExcel(file);
            return ResponseEntity.ok("{\"message\": \"Carga masiva de usuarios completada exitosamente.\"}");
        } catch (Exception e) {
            e.printStackTrace();
            String errorMessage = String.format("{\"error\": \"Error durante la carga masiva: %s\"}", e.getMessage());
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).contentType(MediaType.APPLICATION_JSON).body(errorMessage);
        }
    }
}




```